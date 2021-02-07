
FROM maven:3.5.2-jdk-8-alpine AS MAVEN_TOOL_CHAIN
COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn package
 
FROM tomcat:7.0-jre8-alpine
COPY --from=MAVEN_TOOL_CHAIN /tmp/target/cinema*.war $CATALINA_HOME/webapps/cinema.war

 
# set the startup command to execute the jar
HEALTHCHECK --interval=1m --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:8080/cinema/movies || exit 1