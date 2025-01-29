const { test, expect } = require("playwright/test");
const { userLogin,baseUrl,authFile } = require("./loginPage");


test('Login Page', async ({ page }) => {

    //const baseUrl = "https://crm.testsjit.in/#/login";
    await page.goto(baseUrl);
    const userId = "4"
    const password = "13$HiV@M97J"
    userLogin(page, userId, password)
    await page.waitForTimeout(10000);

    await page.context().storageState({ path: authFile });
})