FROM apluslms/run-mooc-grader:1.4
COPY *.whl /roman/

RUN apt_install sqlite3 libsqlite3-dev sudo \
&& pip3 install Docker \
&& pip3 install /roman/apluslms_yamlidator-0.3.0a1-py3-none-any.whl \
&& pip3 install /roman/apluslms_roman-0.3.0a1-py3-none-any.whl
COPY grader-cont-settings.py /srv/
COPY grader-init.sh /srv/
COPY local_settings.py /srv/grader/
COPY cron_pull_build.sh cron.sh /srv/grader/gitmanager/
COPY rootfs/etc/services.d/clone_build /etc/services.d/clone_build
COPY rootfs/etc/cont-init.d /etc/cont-init.d
ENV DOCKER_HOST_PATH=/var/lib/docker/volumes/aplus_data/_data/grader/courses/

