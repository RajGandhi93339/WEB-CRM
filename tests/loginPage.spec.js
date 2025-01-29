import { test, expect } from '@playwright/test';
import { loginPage } from '../Pages/loginPage'

const authFile = "config/auth.json";

test('Login Page', async ({ page }) => {

    const login = new loginPage(page);
    await login.gotobaseUrl(page);
    const userId = "4"
    const password = "13$HiV@M97J"
    await login.loginUsers(userId, password)
    await page.waitForTimeout(10000);
    await page.context().storageState({ path: authFile });

})