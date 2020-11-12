import streamlit as st
import textwrap
from streamlit_ace import st_ace
import numpy as np
from typing import List, Sequence, ForwardRef, Union

"# Bootstrap Columns"

IntOrIntSequence = Union[int, Sequence[int]] 
def bootstrap_columns(spec: IntOrIntSequence) -> List[ForwardRef('DeltaGenerator')]:
    """Like beta_columns(...), but you have to specify widths in integer
    increments of 1/12th of the full column."""
    # Special case for fixed width columns
    if type(spec) == int:
        return st.beta_columns(spec)

    col_sum = sum(spec)
    if col_sum > 12:
        raise RuntimeError('Column widths cannot exceed 12.')
    elif col_sum == 12:
        return st.beta_columns(spec)
    if col_sum < 12:
        final_col_width = 12 - col_sum
        extended_columns = tuple(spec) + (final_col_width,)
        return st.beta_columns(extended_columns)[:-1]

"## Try It Out"

default_exec_str = (textwrap.dedent("""
col1, col2, col3 = bootstrap_columns((3, 4, 5))
col1.bar_chart(np.random.rand(10), height=200)
col2.bar_chart(np.random.rand(10), height=200)
col3.bar_chart(np.random.rand(10), height=200)
""".strip()))

exec_str = st_ace(value=default_exec_str, language='python', auto_update=True, height=150)
exec(exec_str)

"## Documentation"

with st.beta_expander('Show bootstrap_columns'):
    st.help(bootstrap_columns)

with st.beta_expander('Show beta_columns'):
    st.help(st.beta_columns)

