/* Reusable quiz widget — shared across lessons.
 *
 * Usage in a lesson:
 *   <div class="quiz" data-answer="1">
 *     <p class="q">질문 텍스트</p>
 *     <button data-i="0">보기 A</button>
 *     <button data-i="1">보기 B</button>
 *     <button data-i="2">보기 C</button>
 *     <p class="explain" hidden>정답 해설 …</p>
 *   </div>
 * data-answer = 정답 버튼의 data-i 값.
 * Immediate feedback: 클릭 즉시 정답/오답 색을 칠하고 해설을 연다.
 */
(function () {
  function grade(quiz, chosen) {
    var answer = parseInt(quiz.getAttribute('data-answer'), 10);
    var buttons = quiz.querySelectorAll('button[data-i]');
    buttons.forEach(function (b) {
      var i = parseInt(b.getAttribute('data-i'), 10);
      b.disabled = true;
      if (i === answer) b.classList.add('correct');
      else if (i === chosen) b.classList.add('wrong');
    });
    var explain = quiz.querySelector('.explain');
    if (explain) explain.hidden = false;
    var verdict = quiz.querySelector('.verdict');
    if (verdict) {
      verdict.hidden = false;
      verdict.textContent = (chosen === answer) ? '정답입니다 ✓' : '다시 생각해볼까요 — 정답은 초록색입니다.';
      verdict.className = 'verdict ' + (chosen === answer ? 'ok' : 'no');
    }
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.quiz button[data-i]');
    if (!btn) return;
    var quiz = btn.closest('.quiz');
    if (quiz.classList.contains('answered')) return;
    quiz.classList.add('answered');
    grade(quiz, parseInt(btn.getAttribute('data-i'), 10));
  });
})();
