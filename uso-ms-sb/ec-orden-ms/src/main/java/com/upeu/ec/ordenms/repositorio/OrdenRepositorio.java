package com.upeu.ec.ordenms.repositorio;

import com.upeu.ec.ordenms.entidad.Orden;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrdenRepositorio extends JpaRepository<Orden, Long> {
}
