/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.persistence;

import com.essence.model.AnomalyTargetType;
import com.essence.model.Setting;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;
import java.util.List;

/**
 * Created by BWintemberg on 11/1/2015.
 */
public class SettingDAO {
    EntityManagerFactory entityManagerFactory;

    public Setting getSetting(String settingName) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        Query query = entityManager.createQuery("SELECT s from Setting s where name = :settingName");
        query.setParameter("settingName", settingName);

        List<Setting> list = query.getResultList();
        entityManager.close();
        if (list != null && list.size() > 0) {
            return list.get(0);
        }
        return null;
    }

    public void updateSetting(String settingName, String value) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        entityManager.getTransaction().begin();
        Query query = entityManager.createQuery("SELECT s from Setting s where name = :settingName");
        query.setParameter("settingName", settingName);
        List<Setting> results = query.getResultList();
        Setting setting;
        if (results.size() > 0) {
            setting = results.get(0);
        }
        else {
            setting = new Setting();
            setting.setName(settingName);
        }
        setting.setValue(value);
        entityManager.persist(setting);
        entityManager.flush();
        entityManager.getTransaction().commit();
        entityManager.close();
    }

    public EntityManagerFactory getEntityManagerFactory()
    {
        return entityManagerFactory;
    }

    public void setEntityManagerFactory(EntityManagerFactory entityManagerFactory)
    {
        this.entityManagerFactory = entityManagerFactory;
    }
}
