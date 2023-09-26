const pt = require('puppeteer')

async function getText(){
  const browser = await pt.launch();
  const page = await browser.newPage()

  // Navega a la URL del sitio web que deseas raspar
  await page.goto('https://www.sportium.es/apuestas/sports/soccer/competitions/45211');

  let texts = await page.evaluate(() => {
    let data = [];
    let elements = document.getElementsByClassName('btn_action_login');
    for (var element of elements)
      data.push(element.textContent);
    return data;
});
  // const partidos = document.getElementsByClassName('ta-FlexPane')

  //const title = await (await t.getProperty('textContent'))

  // Cierra el navegador
  await browser.close();

  // Devuelve los resultados en formato JSON
  console.log(JSON.stringify(texts));
}

getText()