const x = document.querySelector('.x')
const y = document.querySelector('.y')
const drawSubmit = document.querySelector('.drawSubmit')

function createCanvas() {
  const canvas = document.getElementById('canvas')
  const ctx = canvas.getContext('2d')
  ctx.fillStyle = 'green'
  ctx.fillRect(10, 10, Number(x.value), Number(y.value))
}

drawSubmit.addEventListener('click', createCanvas)
