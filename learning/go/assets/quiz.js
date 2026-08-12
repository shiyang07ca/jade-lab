/* 共享测验组件：课程中所有 .quiz 块依赖此脚本
   用法：<div class="quiz" data-answer="2" data-feedback="解析...">
         <p class="quiz-question">问题</p>
         <ul class="quiz-options">
           <li>选项A</li>...
         </ul>
         <p class="quiz-feedback"></p>
       </div>
   data-answer 为正确选项下标（从 0 起）。 */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quiz').forEach(function (quiz) {
      var correct = parseInt(quiz.getAttribute('data-answer'), 10);
      var options = quiz.querySelectorAll('.quiz-options li');
      var feedback = quiz.querySelector('.quiz-feedback');
      options.forEach(function (opt, i) {
        opt.addEventListener('click', function () {
          options.forEach(function (o) { o.classList.remove('correct', 'wrong'); });
          if (i === correct) {
            opt.classList.add('correct');
            feedback.innerHTML = '<span class="correct-txt">✓ 正确。</span> ' +
              quiz.getAttribute('data-feedback');
          } else {
            opt.classList.add('wrong');
            feedback.innerHTML = '<span class="wrong-txt">✗ 不对，再想想。</span> ' +
              quiz.getAttribute('data-feedback');
          }
        });
      });
    });
  });
})();
