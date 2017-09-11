from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3117   ._SN',
            'ED6_DT01/T3117_1 ._SN',
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
        'Ray',                                  # 9
        'Terry',                                # 10
        'Antoine',                              # 11
        'Sneaker',                              # 12
        'Book',                                 # 13
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


    AddCharChip(
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01700 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01700P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -3620,
        Z                   = 750,
        Y                   = 9560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1441795,
        ChipIndex           = 0x3,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -410,
        Z                   = 800,
        Y                   = 6880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835011,
        ChipIndex           = 0x3,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 770,
        TriggerZ            = 0,
        TriggerY            = 14240,
        TriggerRange        = 1200,
        ActorX              = 770,
        ActorZ              = 0,
        ActorY              = 14240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4600,
        TriggerZ            = 1000,
        TriggerY            = 12780,
        TriggerRange        = 1200,
        ActorX              = 5880,
        ActorZ              = 2000,
        ActorY              = 13200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -410,
        TriggerZ            = 0,
        TriggerY            = 6880,
        TriggerRange        = 1200,
        ActorX              = -410,
        ActorZ              = 800,
        ActorY              = 6880,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1D6",          # 00, 0
        "Function_1_40A",          # 01, 1
        "Function_2_532",          # 02, 2
        "Function_3_548",          # 03, 3
        "Function_4_56C",          # 04, 4
        "Function_5_619",          # 05, 5
        "Function_6_63A",          # 06, 6
        "Function_7_14B8",         # 07, 7
        "Function_8_2629",         # 08, 8
        "Function_9_2696",         # 09, 9
    )


    def Function_0_1D6(): pass

    label("Function_0_1D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_20C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_242")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_278")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_29F")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 500, 0, 2880, 271)
    OP_43(0xA, 0x0, 0x0, 0x3)
    Jump("loc_3DE")

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 4600, 1000, 13110, 69)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2DF")
    Jump("loc_3DE")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2FF")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_33A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_370")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)
    Jump("loc_3DE")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3AB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2790, 0, 9200, 270)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3DE")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1060, 0, 9420, 253)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2800, 0, 9310, 270)

    label("loc_3DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3EE")
    SetChrFlags(0xB, 0x80)

    label("loc_3EE")

    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    ClearChrFlags(0xC, 0x80)

    label("loc_409")

    Return()

    # Function_0_1D6 end

    def Function_1_40A(): pass

    label("Function_1_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, 770, 0, 14240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_4FF")

    label("loc_4FB")

    OP_64(0x0, 0x1)

    label("loc_4FF")

    Jump("loc_506")

    label("loc_502")

    OP_64(0x0, 0x1)

    label("loc_506")

    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_526")
    OP_65(0x2, 0x1)

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_531")
    OP_64(0x1, 0x1)

    label("loc_531")

    Return()

    # Function_1_40A end

    def Function_2_532(): pass

    label("Function_2_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_532")

    label("loc_547")

    Return()

    # Function_2_532 end

    def Function_3_548(): pass

    label("Function_3_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_8D(0xFE, -2990, 4830, 3120, 870, 3000)
    Jump("Function_3_548")

    label("loc_56B")

    Return()

    # Function_3_548 end

    def Function_4_56C(): pass

    label("Function_4_56C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Talk]\x01",                     # 0
            "[Report test results]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_5F9"),
        (1, "loc_603"),
        (SWITCH_DEFAULT, "loc_60D"),
    )


    label("loc_5F9")

    Call(0, 6)
    TalkEnd(0xFE)
    Jump("loc_60D")

    label("loc_603")

    Call(1, 3)
    TalkEnd(0xFE)
    Jump("loc_60D")

    label("loc_60D")

    Return()

    label("loc_611")

    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_4_56C end

    def Function_5_619(): pass

    label("Function_5_619")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_636")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #0
        0xFE,
        "Nya-o...\x02",
    )

    CloseMessageWindow()

    label("loc_636")

    TalkEnd(0xFE)
    Return()

    # Function_5_619 end

    def Function_6_63A(): pass

    label("Function_6_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6D3")
    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "Thanks a lot for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "We've got ourselves some good\x01",
            "hard data we can use to further\x01",
            "our research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Take care, you guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_73A")
    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        (
            "Thanks for your hard work. \x01",
            "You guys really helped me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Take care, you guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8A3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_810")

    ChrTalk(    #6
        0xFE,
        (
            "I've been working my tail off\x01",
            "getting the funding for our\x01",
            "research next term...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "And Ray hits the jackpot with\x01",
            "just that tomato...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I've got to work harder on my\x01",
            "sneakers project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_810")

    OP_A2(0x1)

    ChrTalk(    #9
        0xFE,
        (
            "I can't believe it... We actually\x01",
            "had an inquiry about that bitter\x01",
            "tomato Ray got his hands on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "What's wrong with the world today?\x02",
    )

    CloseMessageWindow()

    label("loc_8A0")

    Jump("loc_14B4")

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_AEB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AB")

    ChrTalk(    #11
        0xFE,
        (
            "I know you've got to tell some\x01",
            "little white lies to get proper\x01",
            "research funding, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Thing is, I'm a terrible liar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I've got to finish my work on that\x01",
            "sneaker project. Make some kind\x01",
            "of production model to show off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE8")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A64")

    ChrTalk(    #14
        0xFE,
        (
            "I know you've got to tell some\x01",
            "little white lies to get proper\x01",
            "research funding, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Of course, the lies Ray's using\x01",
            "in his project are neither white\x01",
            "nor little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE8")

    label("loc_A64")

    OP_A2(0x1)

    ChrTalk(    #16
        0xFE,
        (
            "I know you've got to tell some\x01",
            "little white lies to get proper\x01",
            "research funding, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Thing is, I'm a terrible liar.\x02",
    )

    CloseMessageWindow()

    label("loc_AE8")

    Jump("loc_14B4")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_C89")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBE")

    ChrTalk(    #18
        0xFE,
        "That Ray...he's unbelievable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I have to admit he's getting a\x01",
            "lot of positive reviews on his\x01",
            "research project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I need to step it up on my\x01",
            "sneaker project like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_BBE")


    ChrTalk(    #21
        0xFE,
        "That Ray...he's unbelievable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I have to admit he's getting a\x01",
            "lot of positive reviews on his\x01",
            "research project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I could probably stand to learn\x01",
            "something from his playing\x01",
            "science by ear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C86")

    Jump("loc_14B4")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_E0F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D1B")

    ChrTalk(    #24
        0xFE,
        (
            "Thank goodness the lab didn't\x01",
            "receive any major damage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Well, the tests are done and\x01",
            "we can proceed on schedule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D99")

    ChrTalk(    #26
        0xFE,
        (
            "Thank goodness the lab didn't\x01",
            "receive any major damage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Looks like the research will\x01",
            "stay on schedule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C")

    label("loc_D99")


    ChrTalk(    #28
        0xFE,
        (
            "The lab doesn't seem to be\x01",
            "out of order. What a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It looks like the product samples\x01",
            "are safe, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0C")

    Jump("loc_14B4")

    label("loc_E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E83")
    TalkBegin(0xFE)

    ChrTalk(    #30
        0xFE,
        "Okay, whenever you're ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "We need stress tests, so feel\x01",
            "free to just stomp around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_E83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EF8")
    TalkBegin(0xFE)

    ChrTalk(    #32
        0xFE,
        "Thanks for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "You guys really helped me out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Hope you like the final product!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_F74")
    TalkBegin(0xFE)

    ChrTalk(    #35
        0xFE,
        "How are the sneakers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Be sure to report back here\x01",
            "after you've walked around\x01",
            "in them for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_F74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_F85")
    Call(1, 2)
    Jump("loc_FBC")

    label("loc_F85")

    TalkBegin(0xFE)

    ChrTalk(    #37
        0xFE,
        "Something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Ray's out to lunch.\x02",
    )

    CloseMessageWindow()

    label("loc_FBC")

    Jump("loc_14B4")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1033")
    TalkBegin(0xFE)

    ChrTalk(    #39
        0xFE,
        "Okay, whenever you're ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "We need stress tests, so feel\x01",
            "free to just stomp around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_1033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10A8")
    TalkBegin(0xFE)

    ChrTalk(    #41
        0xFE,
        "Thanks for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "You guys really helped me out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Hope you like the final product!\x02",
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_10A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1124")
    TalkBegin(0xFE)

    ChrTalk(    #44
        0xFE,
        "How are the sneakers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Be sure to report back here\x01",
            "after you've walked around\x01",
            "in them for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_1124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1135")
    Call(1, 2)
    Jump("loc_11C4")

    label("loc_1135")

    TalkBegin(0xFE)

    ChrTalk(    #46
        0xFE,
        (
            "Well, we have our test units\x01",
            "ready. We're just waiting for\x01",
            "the testers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Looks like I need to adjust the\x01",
            "insoles a little bit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    Jump("loc_14B4")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1275")
    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "What a night that was!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "We were rushing to finish our\x01",
            "test units when suddenly\x01",
            "everything just went black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I almost glued the soles onto\x01",
            "the desk!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_136D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_END)), "loc_12D8")

    ChrTalk(    #51
        0xFE,
        "Ouch...ow! My back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Never mind. Just my imagination.\x01",
            "Back to work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136A")

    label("loc_12D8")


    ChrTalk(    #53
        0xFE,
        (
            "Yup, we definitely need to be\x01",
            "more careful with how we sew\x01",
            "the insole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I tried to test them myself, but I\x01",
            "need to do more monitoring...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136A")

    Jump("loc_14B4")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14B4")
    TalkBegin(0xFE)

    ChrTalk(    #55
        0xFE,
        (
            "Recently, Ray had me try some\x01",
            "kind of vile 'anti-nap' food product\x01",
            "sample.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It looks like a tomato,\x01",
            "but it's terribly bitter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "It definitely made me forget any\x01",
            "thoughts of sleep, but now I can't\x01",
            "get the taste out of my mouth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "But that's like calling mousetraps\x01",
            "on your earlobes 'anti-sleep aids.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B4")

    TalkEnd(0xFE)
    Return()

    # Function_6_63A end

    def Function_7_14B8(): pass

    label("Function_7_14B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1570")

    ChrTalk(    #59
        0xFE,
        (
            "Heh heh, I've already gotten requests\x01",
            "for my bitter tomato.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "At this rate we'll have it on\x01",
            "store shelves in no time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Which means more funding!\x01",
            "SCORE!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_1570")

    OP_A2(0x0)

    ChrTalk(    #62
        0xFE,
        (
            "Good luck, good planning...\x01",
            "I guess it doesn't matter which\x01",
            "you use to get results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I've already gotten requests\x01",
            "for that bitter tomato out in\x01",
            "the greenhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "At this rate we'll have it on\x01",
            "store shelves in no time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Which means more funding!\x01",
            "SCORE!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167F")

    Jump("loc_2625")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(    #66
        0xFE,
        (
            "My thesis for next term is going\x01",
            "to move from the plants to the\x01",
            "greenhouse design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Of course, I have nothing even\x01",
            "planned, so I'll just throw a \x01",
            "bunch of numbers on a page.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Serious researchers like myself need\x01",
            "some serious fund-raising skills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_1796")

    OP_A2(0x0)

    ChrTalk(    #69
        0xFE,
        (
            "My thesis for next term is going\x01",
            "to move from the plants to the\x01",
            "greenhouse design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Of course, I have nothing even\x01",
            "planned, so I'll just throw a \x01",
            "bunch of numbers on a page.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I wonder what kind of weird\x01",
            "plants I can come up with next...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1893")

    Jump("loc_2625")

    label("loc_1896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19B0")

    ChrTalk(    #72
        0xFE,
        (
            "Heh heh, I just finished with this\x01",
            "term's thesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Wanna hear the title? It's called 'The Acerbic\x01",
            "Tomato: An Analysis of Greenhouse Horticulture\x01",
            "and its Impact on Nutritional Balance in Food.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I'm so good at making this stuff\x01",
            "up, I even amaze myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B00")

    label("loc_19B0")

    OP_A2(0x0)

    ChrTalk(    #75
        0xFE,
        "There we go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Morning! I just finished with this\x01",
            "term's thesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Wanna hear the title? It's called 'The Acerbic\x01",
            "Tomato: An Analysis of Greenhouse Horticulture\x01",
            "And Its Impact on Nutritional Balance in Food.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Just rolls right off the tongue,\x01",
            "doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I'm so good at making this stuff up,\x01",
            "I even amaze myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B00")

    Jump("loc_2625")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_1BFD")

    ChrTalk(    #80
        0xFE,
        "I heard the Capel got taken...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "But my tomatoes are just fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I was secretly hoping one of the terrorists'd\x01",
            "come in here and have a taste of one...\x01",
            "Maybe then I could market it as a weapon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "But not a bite mark anywhere.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2625")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1DBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C9D")

    ChrTalk(    #84
        0xFE,
        (
            "That Terry...he's been getting\x01",
            "quite an attitude of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I mean, you'd think he'd be more\x01",
            "appreciative, working so close\x01",
            "to genius!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB9")

    label("loc_1C9D")

    OP_A2(0x0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #86
        0xFE,
        (
            "Terry, you know the proposal \x01",
            "deadline for next term's thesis\x01",
            "is coming up, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "What should I do? Got any\x01",
            "brainstorms for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x9)

    ChrTalk(    #88
        0x9,
        "Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "I'm pretty busy right now.\x01",
            "Come up with something\x01",
            "on your own.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_4B(0x9, 255)

    label("loc_1DB9")

    Jump("loc_2625")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2065")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(    #90
        0xFE,
        (
            "The incident last night was pretty\x01",
            "fascinating, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Everyone's calling it some kind\x01",
            "of disaster, but surely someone\x01",
            "got something from it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2062")

    label("loc_1E69")

    OP_A2(0x0)

    ChrTalk(    #92
        0xFE,
        (
            "The incident last night was pretty\x01",
            "fascinating, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I heard there was some kind of\x01",
            "interference with the orbal generators.\x01",
            "That was news to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Everyone's calling it some kind\x01",
            "of disaster, but surely someone\x01",
            "got something from it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #95
        0xFE,
        "What do you think, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x107,
        "#064FY-Yes!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x107,
        "#562FVery fascinating!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I'm sure I could've guessed you'd\x01",
            "say that. You do take after\x01",
            "Professor Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Terry is a completely different\x01",
            "story, though. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_2062")

    Jump("loc_2625")

    label("loc_2065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_24C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2151")

    ChrTalk(    #100
        0xFE,
        (
            "That Terry...I wish he'd keep his\x01",
            "big mouth shut sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I wanted to see your cute little\x01",
            "face get all scrunched up when\x01",
            "you tried this tomato.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#509F(Wow. They don't let this one\x01",
            "out much, do they...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BD")

    label("loc_2151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_END)), "loc_2206")

    ChrTalk(    #103
        0xFE,
        (
            "Well, if you're not going to try\x01",
            "one, Tita, then I don't have any\x01",
            "more use for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'll leave them there in the\x01",
            "greenhouse if you want to \x01",
            "take some with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BD")

    label("loc_2206")

    OP_A2(0x0)
    OP_A2(0x587)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223B")

    ChrTalk(    #105
        0xFE,
        "Tita! You're just in time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2291")

    label("loc_223B")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #106
        0xFE,
        (
            "Well, well, well.\x01",
            "If it isn't cute little Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "You're just in time!\x02",
    )

    CloseMessageWindow()

    label("loc_2291")


    ChrTalk(    #108
        0x107,
        "#560FIn time for what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I've just developed a very, um,\x01",
            "INTERESTING agricultural specimen\x01",
            "in the greenhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I'd very much like for you to try\x01",
            "it and give your opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "What do you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        (
            "#065FUm...\x02\x03",

            "Is this 'specimen' you're talking\x01",
            "about a...tomato?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "That's right! How did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x107,
        (
            "#060FI just talked to Terry.\x02\x03",

            "He told me something about you\x01",
            "trying to feed him some kind of\x01",
            "bitter tomato.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "...Did he now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x107,
        (
            "#064FWhoops, look at the time!\x01",
            "I have to finish this tour!\x02\x03",

            "I'm sorry, Ray. I'll talk to you\x01",
            "later on, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BD")

    Jump("loc_2625")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2625")

    ChrTalk(    #117
        0xFE,
        (
            "This term I was supposed to be\x01",
            "studying greenhouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Do you know what 'studying greenhouses' means? \x01",
            "Quite literally, you are watching the grass grow.\x01",
            "Boring, and more importantly, unmarketable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "So, I decided to breed a new\x01",
            "species of tomato. It rescued\x01",
            "me, so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "So, heh heh heh...who would like\x01",
            "to sample my tomato, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2625")

    TalkEnd(0xFE)
    Return()

    # Function_7_14B8 end

    def Function_8_2629(): pass

    label("Function_8_2629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2695")
    OP_A2(0x5)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #121
        "\x07\x00Received \x07\x02Acerbic Tomato\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x385, 1)
    OP_64(0x1, 0x1)
    TalkEnd(0xFF)

    label("loc_2695")

    Return()

    # Function_8_2629 end

    def Function_9_2696(): pass

    label("Function_9_2696")

    EventBegin(0x0)
    OP_A2(0x54B)
    OP_64(0x0, 0x1)
    OP_2B(0x41, 0x1)
    OP_6D(770, 0, 14240, 1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B01")
    OP_A2(0x52F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2747")

    ChrTalk(    #122
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, that's...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BB")

    label("loc_2747")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(    #124
        0x101,
        (
            "#004FHey...\x01",
            "Joshua, look at this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#012FYeah. Looks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BB")

    label("loc_27D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2861")

    ChrTalk(    #126
        0x107,
        (
            "#065FHey...\x01",
            "Joshua! What's this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#012FLooks like a smoke canister...\x01",
            "Like that one the sky bandits\x01",
            "used before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BB")

    label("loc_2861")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BB")

    ChrTalk(    #128
        0x106,
        "#057FThis is...a smoke canister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        "#012FAgate, let me see that a sec.\x02",
    )

    CloseMessageWindow()

    label("loc_28BB")

    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #130
        "\x07\x05Joshua quickly dismantled the smoke canister.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x102, -160, 0, 14080, 90)
    SetChrPos(0x101, -420, 0, 15020, 129)
    SetChrPos(0x107, -1610, 0, 13920, 104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_2946")
    SetChrPos(0x106, -1390, 0, 12660, 34)

    label("loc_2946")

    FadeToBright(600, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A27")

    ChrTalk(    #131
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#012FThere are probably more canisters\x01",
            "like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AFE")

    label("loc_2A27")

    OP_A2(0x53E)

    ChrTalk(    #135
        0x101,
        (
            "#501FWhoa...\x01",
            "The smoke's cleared up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x107,
        "#560FWow, that was cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFE")

    Jump("loc_2C3A")

    label("loc_2B01")

    FadeToDark(600, 0, -1)

    AnonymousTalk(    #139
        "\x07\x05Joshua quickly dismantled the smoke canister.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetChrPos(0x102, -160, 0, 14080, 90)
    SetChrPos(0x101, -420, 0, 15020, 129)
    SetChrPos(0x107, -1610, 0, 13920, 104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_2B94")
    SetChrPos(0x106, -1390, 0, 12660, 34)

    label("loc_2B94")

    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C3A")
    OP_A2(0x53E)

    ChrTalk(    #140
        0x106,
        "#052FHuh... Neat trick, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#012FThere are probably more\x01",
            "canisters like this around.\x02\x03",

            "Let's find them, and I'll take\x01",
            "them apart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3A")

    EventEnd(0x0)
    Return()

    # Function_9_2696 end

    SaveToFile()

Try(main)
