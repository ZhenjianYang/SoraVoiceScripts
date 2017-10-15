from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3117_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3117_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_4CA",          # 01, 1
        "Function_2_51F",          # 02, 2
        "Function_3_574",          # 03, 3
        "Function_4_5C9",          # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14E6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1298), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14B")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x157C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x150E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CA")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1176), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x37D2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_249")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_249")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x31D8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C8")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C8")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    LoadEffect(0x0, "map\\\\mp108_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF4240), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3")
    EventBegin(0x1)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_END)),
        (1, "loc_3B2"),
        (2, "loc_3B9"),
        (3, "loc_3C0"),
        (4, "loc_3C7"),
        (SWITCH_DEFAULT, "loc_3CE"),
    )


    label("loc_3B2")

    OP_65(0x0, 0x1)
    Jump("loc_3CE")

    label("loc_3B9")

    OP_65(0x1, 0x1)
    Jump("loc_3CE")

    label("loc_3C0")

    OP_65(0x2, 0x1)
    Jump("loc_3CE")

    label("loc_3C7")

    OP_65(0x3, 0x1)
    Jump("loc_3CE")

    label("loc_3CE")

    EventEnd(0x1)
    Jump("loc_4C3")

    label("loc_3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4C4B40), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_42A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05Response very nearby!\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_4C3")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x989680), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_485")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05Response in the vicinity.\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_4C3")

    label("loc_485")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05No response.\x02",
    )

    OP_22(0xAB, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4C3")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_4CA(): pass

    label("Function_1_4CA")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x40)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Return()

    # Function_1_4CA end

    def Function_2_51F(): pass

    label("Function_2_51F")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x80)
    OP_64(0x1, 0x1)
    EventEnd(0x1)
    Return()

    # Function_2_51F end

    def Function_3_574(): pass

    label("Function_3_574")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x100)
    OP_64(0x2, 0x1)
    EventEnd(0x1)
    Return()

    # Function_3_574 end

    def Function_4_5C9(): pass

    label("Function_4_5C9")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x200)
    OP_64(0x3, 0x1)
    EventEnd(0x1)
    Return()

    # Function_4_5C9 end

    SaveToFile()

Try(main)
