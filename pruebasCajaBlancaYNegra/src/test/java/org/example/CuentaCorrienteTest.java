package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CuentaCorrienteTest {

    CuentaCorriente cuentaCorriente = new CuentaCorriente("pedro", 4325, 7800);
    @Test
    void deposit() {
        assertTrue(cuentaCorriente.deposit(4800));
        assertFalse(cuentaCorriente.deposit(-4800));
    }

    @Test
    void withdraw() {
        assertTrue(cuentaCorriente.withdraw(30, 400));
        assertFalse(cuentaCorriente.withdraw(30, 4000));
        assertFalse(cuentaCorriente.withdraw(30, -400));
    }

    @Test
    void addInterest() {
        cuentaCorriente.addInterest();
        assertEquals(8151, cuentaCorriente.getSaldo());
        assertNotEquals(527, cuentaCorriente.getSaldo(), "El sueldo con el interes debe ser 8151");
    }

    @Test
    void getSaldo() {
        assertEquals(7800, cuentaCorriente.getSaldo());
        assertNotEquals(527, cuentaCorriente.getSaldo(), "El sueldo con el interes debe ser 8151");
    }

    @Test
    void getAccountNumber() {
        assertEquals(4325, cuentaCorriente.getAccountNumber());
        assertNotEquals(527, cuentaCorriente.getAccountNumber());
    }

    @Test
    void testToString() {
    }
}