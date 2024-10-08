# Домашнее задание к занятию 16 «Платформа мониторинга Sentry»

## Задание 1

Так как Self-Hosted Sentry довольно требовательная к ресурсам система, мы будем использовать Free Сloud account.

Free Cloud account имеет ограничения:

- 5 000 errors;
- 10 000 transactions;
- 1 GB attachments.

Для подключения Free Cloud account:

- зайдите на sentry.io;
- нажмите «Try for free»;
- используйте авторизацию через ваш GitHub-аккаунт;
- далее следуйте инструкциям.

В качестве решения задания пришлите скриншот меню Projects.

<img width="1242" alt="Projects" src="https://github.com/user-attachments/assets/baa239c7-fe38-4214-a82a-1f69db7ea911">

<img width="1247" alt="Created Project" src="https://github.com/user-attachments/assets/95a8117f-c118-4589-9d4c-42ed86b9b57e">


## Задание 2

1. Создайте python-проект и нажмите `Generate sample event` для генерации тестового события.

<img width="446" alt="Script" src="https://github.com/user-attachments/assets/b58977d7-882a-4781-80c2-5b847ab8fde4">

<img width="1016" alt="Issues" src="https://github.com/user-attachments/assets/3e944a72-258c-4f85-9ba9-dc25fcb06916">

2. Изучите информацию, представленную в событии.

<img width="1189" alt="Inf issues" src="https://github.com/user-attachments/assets/3f879884-76a7-417d-b20b-da2ba85a072c">

<img width="932" alt="Zero Division" src="https://github.com/user-attachments/assets/5335eb70-6fc4-457d-8ebc-1e5061b5db26">

3. Перейдите в список событий проекта, выберите созданное вами и нажмите `Resolved`.
4. В качестве решения задание предоставьте скриншот `Stack trace` из этого события и список событий проекта после нажатия `Resolved`.

<img width="1152" alt="Stack trace" src="https://github.com/user-attachments/assets/9fa46ad6-d35d-45c6-bcc9-2c22768785a7">

## Задание 3

1. Перейдите в создание правил алёртинга.
2. Выберите проект и создайте дефолтное правило алёртинга без настройки полей.
3. Снова сгенерируйте событие `Generate sample event`.
Если всё было выполнено правильно — через некоторое время вам на почту, привязанную к GitHub-аккаунту, придёт оповещение о произошедшем событии.
4. Если сообщение не пришло — проверьте настройки аккаунта Sentry (например, привязанную почту), что у вас не было 
`sample issue` до того, как вы его сгенерировали, и то, что правило алёртинга выставлено по дефолту (во всех полях all).
Также проверьте проект, в котором вы создаёте событие — возможно алёрт привязан к другому.
5. В качестве решения задания пришлите скриншот тела сообщения из оповещения на почте.
6. Дополнительно поэкспериментируйте с правилами алёртинга. Выбирайте разные условия отправки и создавайте sample events. 

<img width="776" alt="Alert post" src="https://github.com/user-attachments/assets/791fb62d-6eee-4486-ac98-1b720fafa94a">

## Задание повышенной сложности

1. Создайте проект на ЯП Python или GO (около 10–20 строк), подключите к нему sentry SDK и отправьте несколько тестовых событий.
2. Поэкспериментируйте с различными передаваемыми параметрами, но помните об ограничениях Free учётной записи Cloud Sentry.
3. В качестве решения задания пришлите скриншот меню issues вашего проекта и пример кода подключения sentry sdk/отсылки событий.

[python-project](https://github.com/sash3939/Monitoring-Sentry/blob/main/python-project.py)


<img width="1164" alt="Python project" src="https://github.com/user-attachments/assets/5e7adbfa-207d-4b88-8469-f81a5e9cc2e4">


<img width="311" alt="Test event" src="https://github.com/user-attachments/assets/90a2534b-6f97-4524-b129-6ff52f025aee">


<img width="471" alt="Test error" src="https://github.com/user-attachments/assets/8e40ca10-efdd-4b5d-8554-7b8e09cdbcd7">


<img width="826" alt="Test-event Post" src="https://github.com/user-attachments/assets/be31b6b5-1228-4b19-89a6-fb7397234e13">


<img width="698" alt="Test-error Post" src="https://github.com/user-attachments/assets/e638912b-1203-4e51-b85a-ba106a926c61">

---

