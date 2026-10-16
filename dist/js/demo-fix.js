/* Demo touch-ups, applied in the browser to the HTML the demo backend returns.
   1. Trades the backend has no photo set for (power washing, pool service, tree service)
      get photos from Dominion's own lead sites: /demo-images/<folder>/1-4.jpg.
   2. Footer links run left to right in rows instead of one long column. */
(function () {
  var TRADES = [
    { folder: "power-washing", re: /pressure\s*wash|power\s*wash|soft\s*wash|driveway clean|house wash|fence clean|roof clean|exterior clean/i },
    { folder: "pool", re: /\bpools?\b|\bspa\b|swimming/i },
    { folder: "tree", re: /\btrees?\b|stump|arborist|limb removal|land clearing/i }
  ];
  var FOOTER_CSS =
    '<style id="dwdp-footer-rows">' +
    "footer ul,footer ol{display:flex!important;flex-wrap:wrap!important;gap:6px 22px!important;list-style:none!important;padding-left:0!important;margin-left:0!important}" +
    "footer li{display:inline-block!important;margin:0!important}" +
    "footer nav{display:flex!important;flex-wrap:wrap!important;gap:6px 22px!important}" +
    "footer nav a{display:inline-block!important}" +
    "</style>";

  function pickFolder(hints) {
    var text = (hints || []).join(" ");
    for (var i = 0; i < TRADES.length; i++) {
      if (TRADES[i].re.test(text)) return TRADES[i].folder;
    }
    return null;
  }

  window.dwdpFixDemo = function (html, hints) {
    if (typeof html !== "string") return html;
    try {
      var folder = pickFolder(hints);
      if (folder) {
        html = html.replace(/(demo-images\/)[a-z0-9-]+\/(\d+)\.jpg/g, function (m, pre, n) {
          var k = ((parseInt(n, 10) - 1) % 4 + 4) % 4 + 1;
          return pre + folder + "/" + k + ".jpg";
        });
      }
      if (html.indexOf("dwdp-footer-rows") === -1) {
        html = html.indexOf("</head>") !== -1 ? html.replace("</head>", FOOTER_CSS + "</head>") : FOOTER_CSS + html;
      }
    } catch (e) { /* never block the preview */ }
    return html;
  };
})();
