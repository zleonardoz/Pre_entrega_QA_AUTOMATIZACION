import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()

        # Obtenemos el nombre del primer producto en la tienda
        primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name" ).text

        # Añadir el primer producto al carrito haciendo clic en el botón correspondiente
        boton_agregar = driver.find_element(By.CSS_SELECTOR, ".inventory_item button")
        boton_agregar.click()

        # Verificar que el contador del carrito se incremente (sea '1')
        badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        
        assert (badge_carrito.text == "1"), f"Se espera '1'  el numero pero fue '{badge_carrito.text}'"

        # Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Comprobar que el producto añadido aparezca correctamente en el carrito
        producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        
        assert (producto_en_carrito == primer_producto_nombre), f"Se espera '{primer_producto_nombre}', pero apareció '{producto_en_carrito}'"

    finally:
        driver.quit()