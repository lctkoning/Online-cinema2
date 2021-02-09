
FROM maven:3.5.2-jdk-8-alpine AS MAVEN_TOOL_CHAIN
COPY pom.xml /tmp/
COPY src /tmp/src/
WORKDIR /tmp/
RUN mvn package
 

FROM tomcat:7.0-jre8-alpine
COPY --from=MAVEN_TOOL_CHAIN /tmp/target/cinema*.war /usr/local/tomcat/webapps/cinema1.war
CMD ["catalina.sh","run"]
