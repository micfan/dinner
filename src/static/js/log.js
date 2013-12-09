/**
 * Created by mic on 5/21/15.
 */

window.mic = window.mic || {};


function reportFEError(message, url, line) {
  if (!window.mic.DEBUG) {
    var img = new Image();
    var qs = ['?message=', message, '&url=', url, '&line=', line].join('');
    img.src = window.mic.url.FEExceptionReport + qs;
  } else if (typeof window.console === 'object') {
    window.console.error(message, url, line);
  }
}

window.mic.log = null;

window.onerror = reportFEError;



//throw 'admin';


