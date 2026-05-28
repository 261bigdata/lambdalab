package com.upeu.ec.pagoms.repositorio;

import com.upeu.ec.pagoms.entidad.Pago;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PagoRepositorio extends JpaRepository<Pago, Long> {
}
