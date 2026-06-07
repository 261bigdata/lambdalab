package com.upeu.ec.ordenms.repository;

import com.upeu.ec.ordenms.entity.Orden;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrdenRepositorio extends JpaRepository<Orden, Long> {
}
