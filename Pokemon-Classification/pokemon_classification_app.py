import streamlit as st

def is_legend_rules_based(egg_type_1, growth_rate, catch_rate, egg_cycles, is_genderless):
    legend_egg_types = {'undiscovered', 'fairy'}
    egg_cycles_thresh = 80
    non_legend_growths = {'erratic', 'fluctuating', 'fast', 'medium fast'}
    non_legend_catch_rate = range(46, 255)
    leg = 'Legendary'
    not_leg = 'Not Legendary'
    if egg_type_1 not in legend_egg_types:
        return not_leg
    elif growth_rate in non_legend_growths:
        return not_leg
    elif catch_rate in non_legend_catch_rate:
        return not_leg
    elif egg_cycles >= egg_cycles_thresh:
        return leg
    elif (egg_type_1 in legend_egg_types) & (is_genderless == True):
        return leg
    else:
        return not_leg

if __name__ == '__main__':
    # Overall Header
    st.title('Pokemon Classification')

    # Sidebar with options
    st.sidebar.subheader('Choose Pokemon Stats')
    cr = st.sidebar.number_input(label='Catch Rate', min_value=3, max_value=255, value=120)
    ec = st.sidebar.number_input(label='Egg Cycles', min_value=5, max_value=120, value=55)
    gr = st.sidebar.selectbox(label='Growth Rate', options=['fast', 'medium fast', 'medium slow', 'slow', 'erratic', 'fluctuating'])
    et1 = st.sidebar.selectbox(label='Egg Type 1', options=['undiscovered', 'fairy', 'other'])
    gl = st.sidebar.radio(label='Genderless', options=[True, False])

    # Space to show the selected statistics
    st.metric('Catch Rate', cr)
    st.metric('Egg Cycles', ec)
    st.metric('Growth Rate', gr)
    st.metric('Egg Type 1', et1)
    st.metric('Genderless', gl)

    # Space to display classification
    st.subheader('_Legendary Pokemon Classification Prediction:_')
    st.write(f'## {is_legend_rules_based(et1, gr, cr, ec, gl)}')