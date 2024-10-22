library(tidyverse)
library(ggplot2)
library(plotly)

# Read command-line arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
model_results_file <- args[2]
output_file <- args[3]

# Load data
data <- read_csv(input_file)
model_results <- read_lines(model_results_file)

# Create advanced visualizations
plot_temperature_humidity <- function(data) {
  p <- ggplot(data, aes(x = temp, y = humid, color = fire)) +
    geom_point(alpha = 0.6) +
    geom_smooth(method = "lm", se = FALSE) +
    facet_wrap(~region) +
    labs(title = "Temperature vs Humidity by Region and Fire Occurrence",
         x = "Temperature", y = "Humidity") +
    theme_minimal()
  return(ggplotly(p))
}

plot_fwi_components <- function(data) {
  data_long <- data %>%
    select(FFMC, DMC, DC, ISI, BUI, FWI) %>%
    gather(key = "component", value = "value")
  
  p <- ggplot(data_long, aes(x = component, y = value, fill = component)) +
    geom_violin() +
    geom_boxplot(width = 0.1, color = "black", alpha = 0.2) +
    labs(title = "Distribution of Fire Weather Index Components",
         x = "Component", y = "Value") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  return(ggplotly(p))
}

plot_fire_probability <- function(data) {
  p <- ggplot(data, aes(x = FWI, y = as.numeric(fire), color = region)) +
    geom_point(alpha = 0.6) +
    geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
    labs(title = "Fire Probability vs Fire Weather Index by Region",
         x = "Fire Weather Index (FWI)", y = "Fire Probability") +
    theme_minimal()
  return(ggplotly(p))
}

# Generate plots
temp_humid_plot <- plot_temperature_humidity(data)
fwi_components_plot <- plot_fwi_components(data)
fire_prob_plot <- plot_fire_probability(data)

# Combine plots and save
combined_plot <- subplot(temp_humid_plot, fwi_components_plot, fire_prob_plot, nrows = 3)
combined_plot <- combined_plot %>% layout(title = "Forest Fire Analysis Visualizations")

# Save the plot as an HTML file
htmlwidgets::saveWidget(combined_plot, output_file)

# Print model results to console
cat(model_results, sep = "\n")