def tax_projection(total_value, tax_rate=0.15):
    return {"tax_rate": tax_rate, "estimated_tax": total_value * tax_rate}
