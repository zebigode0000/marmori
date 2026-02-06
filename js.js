const observer = new IntersectionObserver((entries) => {
  // Filtra apenas os elementos que acabaram de entrar na tela
  const entrando = entries.filter(entry => entry.isIntersecting);

  entrando.forEach((entry, index) => {
    // Pegamos a animação do data-anim
    const animacao = entry.target.getAttribute('data-anim');

    // Se houver muitos elementos entrando ao mesmo tempo (como no refresh),
    // a gente usa o index para o delay. Se for só um (rolando a página), é instantâneo.
    setTimeout(() => {
      if (animacao) {
        entry.target.classList.add(animacao);
      }
      entry.target.classList.remove('esconder');
      observer.unobserve(entry.target);
    }, index * 150); // Reduzi para 150ms para ser mais fluido
  });
}, { 
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px' // Faz disparar um pouco antes de chegar no elemento
});

document.querySelectorAll('.esconder').forEach(el => observer.observe(el));