// Shared quiz widget. Buttons carry data-correct="true|false".
// Optional per-quiz feedback via data-ok / data-no on the .quiz element.
document.querySelectorAll('.quiz').forEach(function (q) {
  var fb = q.querySelector('.fb');
  var okMsg = q.dataset.ok || '정답!';
  var noMsg = q.dataset.no || '다시 생각해 보세요.';
  q.querySelectorAll('button').forEach(function (b) {
    b.addEventListener('click', function () {
      var ok = b.dataset.correct === 'true';
      b.classList.add(ok ? 'correct' : 'wrong');
      if (fb) fb.textContent = ok ? okMsg : noMsg;
    });
  });
});
