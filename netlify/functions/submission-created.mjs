// Texts Maurice about every verified Netlify Forms submission on this site.
//
// Netlify runs this automatically after a form submission passes its spam filter
// (the "submission-created" event). It tidies the fields into one simple shape and posts
// them to the GoHighLevel workflow "Website Form - Text Maurice", which saves the lead as
// a contact and sends the text from the A2P-approved number.
//
// The workflow address lives in the FORM_TEXT_WEBHOOK environment variable in Netlify,
// not in this public repo. If it is missing or GoHighLevel is down, the form still saves
// and the usual email still goes out; this function never blocks a submission.

const FORM_LABELS = {
  "homepage-contact": "Contact form",
  "site-check": "Free Site Check",
  "client-intake": "Client intake form",
};

const pick = (data, keys) => {
  for (const k of keys) {
    const v = data[k];
    if (typeof v === "string" && v.trim()) return v.trim();
  }
  return "";
};

const toE164 = (raw) => {
  const digits = (raw || "").replace(/\D/g, "");
  if (digits.length === 10) return "+1" + digits;
  if (digits.length === 11 && digits.startsWith("1")) return "+" + digits;
  return raw || "";
};

export function buildLead(payload) {
  const data = payload.data || {};
  const formName = payload.form_name || data["form-name"] || "form";
  const label = FORM_LABELS[formName] || formName;
  let host = "your website";
  try { host = new URL(payload.site_url || data.referrer || "").hostname.replace(/^www\./, ""); } catch {}

  const name = pick(data, ["name", "Your name"]) || pick(data, ["business", "Business name"]);
  const [first, ...rest] = name.split(/\s+/);
  const phone = toE164(pick(data, ["phone", "Your phone", "Lead text phone", "Public phone"]));
  const email = pick(data, ["email", "Your email", "Lead email"]);

  let message = pick(data, ["message", "Anything else", "Your story"]);
  if (formName === "site-check") {
    const site = pick(data, ["website"]);
    const grade = pick(data, ["grade"]);
    message = [site && `Checked ${site}`, grade && `grade ${grade}`].filter(Boolean).join(", ") || message;
  }
  if (formName === "client-intake") {
    const pkg = pick(data, ["Package"]);
    const biz = pick(data, ["Business name"]);
    message = [biz, pkg && `package ${pkg}`].filter(Boolean).join(", ") || message;
  }
  const business = pick(data, ["business", "Business name"]);
  if (message.length > 300) message = message.slice(0, 297) + "...";

  return {
    form: label,
    site: host,
    summary: `${label} on ${host}`,
    name: name || "(no name given)",
    first_name: first || "",
    last_name: rest.join(" "),
    phone: phone || "",
    email: email || "",
    business,
    message: message || "(no message)",
  };
}

export const handler = async (event) => {
  try {
    const { payload } = JSON.parse(event.body || "{}");
    const url = process.env.FORM_TEXT_WEBHOOK;
    if (!payload || !url) return { statusCode: 200, body: "skipped" };
    const lead = buildLead(payload);
    const res = await fetch(url, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(lead),
    });
    console.log(`form-text: ${lead.summary} -> GoHighLevel ${res.status}`);
  } catch (err) {
    console.log("form-text failed:", err && err.message);
  }
  return { statusCode: 200, body: "ok" };
};
