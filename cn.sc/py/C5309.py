from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5309   ._SN',
        MapName             = 'Other',
        Location            = 'C5309.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        '瘦狼瓦鲁特',                           # 9
        '瘦狼瓦鲁特',                           # 10
        '血狮',                                 # 11
        '血狮',                                 # 12
        '亡命装甲兵',                           # 13
        '幻惑之铃露茜奥拉',                     # 14
        '目标用照相机',                         # 15
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
        'ED6_DT26/CH20461 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT26/CH20461P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -32500,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = -32500,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_28F",          # 01, 1
        "Function_2_317",          # 02, 2
        "Function_3_494",          # 03, 3
        "Function_4_4FF",          # 04, 4
        "Function_5_70E",          # 05, 5
        "Function_6_97D",          # 06, 6
        "Function_7_12C1",         # 07, 7
        "Function_8_1341",         # 08, 8
        "Function_9_13C1",         # 09, 9
        "Function_10_146E",        # 0A, 10
        "Function_11_151B",        # 0B, 11
        "Function_12_239B",        # 0C, 12
        "Function_13_2429",        # 0D, 13
        "Function_14_249E",        # 0E, 14
        "Function_15_24B4",        # 0F, 15
        "Function_16_2692",        # 10, 16
        "Function_17_26AE",        # 11, 17
        "Function_18_26CA",        # 12, 18
        "Function_19_26E6",        # 13, 19
        "Function_20_2702",        # 14, 20
        "Function_21_31A4",        # 15, 21
        "Function_22_4D41",        # 16, 22
        "Function_23_4DDA",        # 17, 23
        "Function_24_4DF6",        # 18, 24
        "Function_25_4E12",        # 19, 25
        "Function_26_4E2E",        # 1A, 26
        "Function_27_4E4A",        # 1B, 27
        "Function_28_4EB6",        # 1C, 28
        "Function_29_4FCD",        # 1D, 29
        "Function_30_4FFE",        # 1E, 30
        "Function_31_5085",        # 1F, 31
        "Function_32_5118",        # 20, 32
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_230")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -18090, 0, 3500, 180)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 23)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17410, 0, 4440, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 23)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_241")
    OP_A3(0x10F0)
    Event(0, 28)
    Jump("loc_28E")

    label("loc_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26B")
    Event(0, 29)
    Jump("loc_28E")

    label("loc_26B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_28E")

    label("loc_285")

    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_28E")

    Return()

    # Function_0_1B6 end

    def Function_1_28F(): pass

    label("Function_1_28F")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_END)), "loc_2A4")
    OP_64(0x0, 0x1)
    OP_71(0x1, 0x4)

    label("loc_2A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x461), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5")
    Call(0, 4)
    Jump("loc_2D2")

    label("loc_2C5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_2D2")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_28F end

    def Function_2_317(): pass

    label("Function_2_317")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_47E")

    label("loc_33C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_47E")

    label("loc_355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_47E")

    label("loc_36E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_47E")

    label("loc_387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_47E")

    label("loc_3A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_47E")

    label("loc_3B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_47E")

    label("loc_3D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_47E")

    label("loc_3EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_47E")

    label("loc_404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_47E")

    label("loc_41D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_47E")

    label("loc_436")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_47E")

    label("loc_44F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_47E")

    label("loc_468")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_47E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_493")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_47E")

    label("loc_493")

    Return()

    # Function_2_317 end

    def Function_3_494(): pass

    label("Function_3_494")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05瓦鲁特力尽晕倒了。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_494 end

    def Function_4_4FF(): pass

    label("Function_4_4FF")

    OP_D2(0x2701C6, 0x2701CB, 0x1)
    OP_D2(0x290428, 0x29042C, 0x2)
    OP_D2(0x290429, 0x29042D, 0x3)
    OP_D2(0x290188, 0x29018C, 0x4)
    OP_D2(0x290189, 0x29018D, 0x5)
    OP_D2(0x270110, 0x270120, 0x6)
    OP_D2(0x270111, 0x270121, 0x7)
    OP_D2(0x270130, 0x270140, 0x8)
    OP_D2(0x270131, 0x270141, 0x9)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_57E"),
        (5, "loc_595"),
        (3, "loc_5AC"),
        (4, "loc_5C3"),
        (6, "loc_5DA"),
        (8, "loc_5F1"),
        (10, "loc_608"),
        (SWITCH_DEFAULT, "loc_61F"),
    )


    label("loc_57E")

    OP_D2(0x701D0, 0x701DC, 0xA)
    OP_D2(0x701D1, 0x701DD, 0xB)
    Jump("loc_61F")

    label("loc_595")

    OP_D2(0x70218, 0x70224, 0xA)
    OP_D2(0x70219, 0x70225, 0xB)
    Jump("loc_61F")

    label("loc_5AC")

    OP_D2(0x701E8, 0x701F4, 0xA)
    OP_D2(0x701E9, 0x701F5, 0xB)
    Jump("loc_61F")

    label("loc_5C3")

    OP_D2(0x27036E, 0x27037B, 0xA)
    OP_D2(0x27036F, 0x27037C, 0xB)
    Jump("loc_61F")

    label("loc_5DA")

    OP_D2(0x70230, 0x7023C, 0xA)
    OP_D2(0x70231, 0x7023D, 0xB)
    Jump("loc_61F")

    label("loc_5F1")

    OP_D2(0x270176, 0x270183, 0xA)
    OP_D2(0x270177, 0x270184, 0xB)
    Jump("loc_61F")

    label("loc_608")

    OP_D2(0x702B4, 0x702BB, 0xA)
    OP_D2(0x702B5, 0x702BC, 0xB)
    Jump("loc_61F")

    label("loc_61F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_644"),
        (5, "loc_65B"),
        (3, "loc_672"),
        (4, "loc_689"),
        (6, "loc_6A0"),
        (8, "loc_6B7"),
        (10, "loc_6CE"),
        (SWITCH_DEFAULT, "loc_6E5"),
    )


    label("loc_644")

    OP_D2(0x701D0, 0x701DC, 0xC)
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_6E5")

    label("loc_65B")

    OP_D2(0x70218, 0x70224, 0xC)
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_6E5")

    label("loc_672")

    OP_D2(0x701E8, 0x701F4, 0xC)
    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_6E5")

    label("loc_689")

    OP_D2(0x27036E, 0x27037B, 0xC)
    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_6E5")

    label("loc_6A0")

    OP_D2(0x70230, 0x7023C, 0xC)
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_6E5")

    label("loc_6B7")

    OP_D2(0x270176, 0x270183, 0xC)
    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_6E5")

    label("loc_6CE")

    OP_D2(0x702B4, 0x702BB, 0xC)
    OP_D2(0x702B5, 0x702BC, 0xD)
    Jump("loc_6E5")

    label("loc_6E5")

    OP_D2(0x27022A, 0x270234, 0xE)
    OP_D2(0x2600A0, 0x2600A5, 0xF)
    OP_D2(0x260052, 0x260057, 0x10)
    OP_D2(0x2601C4, 0x2601C9, 0x11)
    Return()

    # Function_4_4FF end

    def Function_5_70E(): pass

    label("Function_5_70E")

    OP_D2(0x2701C6, 0x2701CB, 0x1)
    OP_D2(0x290428, 0x29042C, 0x2)
    OP_D2(0x290429, 0x29042D, 0x3)
    OP_D2(0x270110, 0x270120, 0x4)
    OP_D2(0x270111, 0x270121, 0x5)
    OP_D2(0x270130, 0x270140, 0x6)
    OP_D2(0x270131, 0x270141, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779")
    OP_D2(0x701D0, 0x701DC, 0x8)
    OP_D2(0x701D1, 0x701DD, 0x9)
    Jump("loc_854")

    label("loc_779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79E")
    OP_D2(0x70218, 0x70224, 0x8)
    OP_D2(0x70219, 0x70225, 0x9)
    Jump("loc_854")

    label("loc_79E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C3")
    OP_D2(0x701E8, 0x701F4, 0x8)
    OP_D2(0x701E9, 0x701F5, 0x9)
    Jump("loc_854")

    label("loc_7C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E8")
    OP_D2(0x27036E, 0x27037B, 0x8)
    OP_D2(0x27036F, 0x27037C, 0x9)
    Jump("loc_854")

    label("loc_7E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D")
    OP_D2(0x70230, 0x7023C, 0x8)
    OP_D2(0x70231, 0x7023D, 0x9)
    Jump("loc_854")

    label("loc_80D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832")
    OP_D2(0x270176, 0x270183, 0x8)
    OP_D2(0x270177, 0x270184, 0x9)
    Jump("loc_854")

    label("loc_832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")
    OP_D2(0x702B4, 0x702BB, 0x8)
    OP_D2(0x702B5, 0x702BC, 0x9)

    label("loc_854")

    OP_D2(0x7024A, 0x70256, 0xA)
    OP_D2(0x7024C, 0x70258, 0xB)
    OP_D2(0x70251, 0x7025D, 0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88D")
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_92C")

    label("loc_88D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_92C")

    label("loc_8A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C3")
    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_92C")

    label("loc_8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DE")
    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_92C")

    label("loc_8DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F9")
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_92C")

    label("loc_8F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_914")
    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_92C")

    label("loc_914")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92C")
    OP_D2(0x702B5, 0x702BC, 0xD)

    label("loc_92C")

    OP_D2(0x27022A, 0x270234, 0xE)
    OP_D2(0x2600A0, 0x2600A5, 0xF)
    OP_D2(0x2601A7, 0x2601AC, 0x10)
    OP_D2(0x27022C, 0x270236, 0x11)
    OP_D2(0x2601C5, 0x2601CA, 0x12)
    OP_D2(0x260052, 0x260057, 0x13)
    OP_D2(0x70249, 0x70255, 0x14)
    OP_D2(0x70248, 0x70254, 0x15)
    Return()

    # Function_5_70E end

    def Function_6_97D(): pass

    label("Function_6_97D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 4)
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23580, 0, -420, 270)
    SetChrPos(0x102, 23550, 0, 850, 270)
    SetChrPos(0xF8, 24710, 0, -660, 270)
    SetChrPos(0xF9, 24630, 0, 720, 270)

    def lambda_A14():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A14)

    def lambda_A24():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A24)
    Sleep(80)

    def lambda_A44():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A44)
    Sleep(100)

    def lambda_A64():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A64)
    Sleep(150)

    def lambda_A84():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A84)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #2
        0x8,
        "男人的声音",
        "……怎么是你们几个。\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B50")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B8E")

    label("loc_B50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B77")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B8E")

    label("loc_B77")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B8E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BF8")

    label("loc_BBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE1")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BF8")

    label("loc_BE1")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BF8")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_C0A():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C0A)

    def lambda_C22():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C22)

    def lambda_C3A():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C3A)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#1005F#1P『瘦狼』！\x02",
    )

    CloseMessageWindow()

    def lambda_C6D():
        OP_8E(0xFE, 0xFFFFDCEC, 0x0, 0xFFFFFE3E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C6D)

    def lambda_C88():
        OP_6D(-14650, 0, 2440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C88)

    def lambda_CA0():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CA0)

    def lambda_CB8():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CB8)

    def lambda_CC8():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_CC8)
    Sleep(300)

    def lambda_CDD():
        OP_8E(0xFE, 0xFFFFDD82, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDD)
    Sleep(100)

    def lambda_CFD():
        OP_8E(0xFE, 0xFFFFE46C, 0x0, 0xFFFFFBB4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_CFD)
    Sleep(300)
    OP_8E(0xF9, 0xFFFFE444, 0x0, 0x172, 0x1770, 0x0)
    WaitChrThread(0x102, 0x2)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0xF8, 10)
    SetChrChipByIndex(0xF9, 12)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x102,
        (
            "#1042F#6P瓦鲁特……\x01",
            "你是第二道障碍吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#254F#5P哼……\x01",
            "那种无聊事随你怎么说都好。\x02\x03",

            "臭小子，我问你……\x01",
            "金那个混蛋为什么没来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1035F#6P很遗憾，他现在\x01",
            "正在『埃尔赛尤』待命。\x02\x03",

            "#1042F你要是以为他一定会来的话，\x01",
            "那就只能失望了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "#254F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1015F#6P啊，那个……\x01",
            "有需要的话也可以帮你传个话哦～\x02\x03",

            "给雾香小姐也行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#250F#5P啧……臭小鬼，\x01",
            "别多管闲事。\x02\x03",

            "唉，那个蠢大个子竟然没来，\x01",
            "生闷气也没用了……\x02\x03",

            "还是赶快清理掉你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1002F#6P咦……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, -33300, 6900, 2900, 90)
    OP_43(0xA, 0x3, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 2)
    SetChrPos(0xB, -33300, 6900, -2900, 90)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_FD0():
        OP_6D(-31560, 5700, 0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FD0)

    def lambda_FE8():
        OP_67(0, 6700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrPos(0x101, -9130, 0, -310, 270)
    SetChrPos(0x102, -9130, 0, 1050, 270)
    SetChrPos(0xF8, -6990, 0, -720, 270)
    SetChrPos(0xF9, -6990, 0, 1490, 270)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x0, 0x0, 0x9)
    Sleep(100)

    def lambda_1064():
        OP_6D(-13900, 500, 410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1064)

    def lambda_107C():
        OP_67(0, 3000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_107C)

    def lambda_1094():
        OP_6E(288, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1094)

    def lambda_10A4():
        OP_6B(3670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10A4)
    Sleep(100)
    OP_43(0xB, 0x0, 0x0, 0xA)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xB, 0x0)
    Fade(500)

    def lambda_10CF():
        OP_6C(270000, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10CF)
    OP_71(0x0, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #11
        0x8,
        (
            "#252F#5P来吧，小鬼们……\x02\x03",

            "你们就代替金\x01",
            "让我好好享受一番吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_112B():
        OP_6D(-13930, 500, 410, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_112B)

    def lambda_1143():
        OP_67(0, 2800, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1143)

    def lambda_115B():
        OP_6B(3000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_115B)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x8, 16)

    def lambda_117A():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x15E, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_117A)
    Sleep(30)
    OP_44(0xA, 0x3)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1000)

    def lambda_11B5():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11B5)

    def lambda_11C5():
        OP_91(0xFE, 0x1388, 0x0, 0x7D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_11C5)

    def lambda_11E0():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11E0)

    def lambda_11FB():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11FB)
    Sleep(30)
    OP_44(0xB, 0x3)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)

    def lambda_1233():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1233)

    def lambda_1243():
        OP_91(0xFE, 0x1388, 0x0, 0xFFFFF830, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1243)

    def lambda_125E():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_125E)

    def lambda_1279():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1279)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x461, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 11)
    Return()

    # Function_6_97D end

    def Function_7_12C1(): pass

    label("Function_7_12C1")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -18950, 1800, -1850, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_12F2():

        label("loc_12F2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12F2")

    QueueWorkItem2(0xFE, 1, lambda_12F2)

    def lambda_1305():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1305)

    def lambda_1317():
        OP_8F(0xFE, 0xFFFFB5FA, 0x1F4, 0xFFFFF8C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1317)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_7_12C1 end

    def Function_8_1341(): pass

    label("Function_8_1341")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -18950, 1800, 1850, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1372():

        label("loc_1372")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1372")

    QueueWorkItem2(0xFE, 1, lambda_1372)

    def lambda_1385():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1385)

    def lambda_1397():
        OP_8F(0xFE, 0xFFFFB5FA, 0x1F4, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1397)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_8_1341 end

    def Function_9_13C1(): pass

    label("Function_9_13C1")

    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 135, 0)
    ClearChrFlags(0xFE, 0x800)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_13E6():
        OP_99(0xFE, 0x5, 0x7, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E6)

    def lambda_13F6():
        OP_96(0xFE, 0xFFFFAD6C, 0x0, 0xFFFFEB4C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13F6)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 45, 0)

    def lambda_1425():
        OP_99(0xFE, 0x5, 0x7, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1425)

    def lambda_1435():
        OP_96(0xFE, 0xFFFFBF28, 0x0, 0xFFFFF2CC, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1435)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_9_13C1 end

    def Function_10_146E(): pass

    label("Function_10_146E")

    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 45, 0)
    ClearChrFlags(0xFE, 0x800)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1493():
        OP_99(0xFE, 0x5, 0x7, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1493)

    def lambda_14A3():
        OP_96(0xFE, 0xFFFFAD6C, 0x0, 0x1694, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A3)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 135, 0)

    def lambda_14D2():
        OP_99(0xFE, 0x5, 0x7, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D2)

    def lambda_14E2():
        OP_96(0xFE, 0xFFFFBF28, 0x0, 0xF14, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14E2)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_10_146E end

    def Function_11_151B(): pass

    label("Function_11_151B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 4)
    OP_6D(-12230, 0, 1670, 0)
    OP_67(0, 4280, -10000, 0)
    OP_6B(4370, 0)
    SetChrPos(0x101, -13600, 0, -1360, 270)
    SetChrPos(0x102, -13600, 0, -110, 270)
    SetChrPos(0xF8, -12000, 0, -1880, 270)
    SetChrPos(0xF9, -12050, 0, -450, 270)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x102, 8)
    SetChrChipByIndex(0xF8, 10)
    SetChrChipByIndex(0xF9, 12)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -21340, 0, 140, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_72(0x0, 0x4)
    OP_6D(-18640, 0, 1580, 0)
    OP_67(0, 3710, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(379, 0)
    FadeToBright(1000, 0)
    OP_6B(2800, 2000)
    OP_0D()

    ChrTalk(    #12
        0x8,
        (
            "#254F#5P……啧…………\x01",
            "烦人的小鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1019F#6P我，我说……\x01",
            "别老是小鬼小鬼的叫啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(    #14
        0x106,
        (
            "#051F#4P嘿……大叔。\x02\x03",

            "你的脚步好像\x01",
            "有点站不稳了啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_1704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(    #15
        0x10B,
        (
            "#210F#4P的确，像小鬼的家伙\x01",
            "大概也就一个……\x02\x03",

            "可别把我也混为一谈哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1022F#5P你，你啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_1779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E9")

    ChrTalk(    #17
        0x109,
        (
            "#1066F#4P算了算了，艾丝蒂尔。\x01",
            "别发那么大火嘛。\x02\x03",

            "只不过是年近中年的\x01",
            "大叔说些讨厌的话罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_17E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1851")

    ChrTalk(    #18
        0x104,
        (
            "#035F#4P呼，艾丝蒂尔。\x01",
            "就原谅他吧。\x02\x03",

            "#030F只不过是更年期的男人\x01",
            "逞些口舌之能罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_1851")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")

    ChrTalk(    #19
        0x105,
        (
            "#1162F#4P的确，我可能\x01",
            "还不成熟……\x02\x03",

            "但是，想守护自己\x01",
            "所珍视之物的心情却是真实的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_18B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1912")

    ChrTalk(    #20
        0x103,
        (
            "#027F#4P算了算了，艾丝蒂尔。\x02\x03",

            "只不过是更年期的\x01",
            "大叔说些讨厌的话而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1912")


    ChrTalk(    #21
        0x8,
        "#254F#5P啧……胡说八道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1035F#4P……瓦鲁特。\x01",
            "你并没有同我们死缠到底的必要，\x02\x03",

            "#1042F但是我们……\x01",
            "却有必须前进的理由。\x02\x03",

            "即使如此，还是要战下去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1026F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#254F#5P…………………………………\x02\x03",

            "#251F哼……真让人扫兴。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x8, 1)
    Sleep(500)
    SetChrSubChip(0x8, 2)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x0, 0x64)

    def lambda_1A3E():
        OP_6D(-18010, 0, 6140, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A3E)

    def lambda_1A56():
        OP_67(0, 6340, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A56)

    def lambda_1A6E():
        OP_6B(5850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A6E)

    def lambda_1A7E():
        OP_6E(307, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A7E)
    SetChrChipByIndex(0xC, 4)
    SetChrPos(0xC, -45090, 10000, 240, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x20)
    OP_43(0xC, 0x1, 0x0, 0xE)
    OP_8E(0xC, 0xFFFFA9B6, 0x1F40, 0xF0, 0x1770, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B22")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B60")

    label("loc_1B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B49")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B60")

    label("loc_1B49")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B60")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BCA")

    label("loc_1B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB3")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BCA")

    label("loc_1BB3")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1BCA")

    Sleep(1000)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 1)
    Sleep(500)
    SetChrSubChip(0x8, 0)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_96(0x8, 0xFFFFA9B6, 0x157C, 0xFFFFFEAC, 0x1770, 0xFA0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 17)
    Fade(500)
    OP_6D(-34060, 1610, 7700, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6B(4530, 0)
    OP_6C(302000, 0)
    OP_6E(350, 0)
    OP_6D(-30430, 0, 9320, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(4530, 0)
    OP_6C(315000, 0)
    OP_6E(350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x101,
        "#1020F#1P慢、慢着！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#257F#6P……去告诉金。\x01",
            "我和他的胜负留到下次再分。\x02\x03",

            "#253F走了，小鬼们。\x02\x03",

            "可别被『白面』吃掉啊，\x01",
            "多多注意吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D35():
        OP_6D(-17240, 5430, 12640, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1D35)

    def lambda_1D4D():
        OP_67(0, 5540, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D4D)

    def lambda_1D65():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D65)

    def lambda_1D75():
        OP_6E(274, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_1D75)
    SetChrFlags(0x8, 0x20)

    def lambda_1D8A():
        OP_97(0xC, 0xFFFFABFA, 0x1090, 0xFFFEA070, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1D8A)
    OP_97(0x8, 0xFFFFABFA, 0x1090, 0xFFFEA070, 0x1964, 0x1)
    WaitChrThread(0xC, 0x0)
    OP_43(0x8, 0x1, 0x0, 0xF)
    Sleep(1000)
    OP_43(0x8, 0x3, 0x0, 0xC)
    OP_43(0x102, 0x1, 0x0, 0x11)
    Sleep(100)
    OP_43(0x101, 0x1, 0x0, 0x10)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_6D(-18270, 0, 13050, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x101,
        "#1015F#6P……走了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #28
        0x102,
        (
            "#1035F大概是明白没有机会\x01",
            "和金先生进行对决了吧。\x02\x03",

            "#1040F和『怪盗绅士』一样，\x01",
            "这次看来是完全收手了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #29
        0x101,
        "#1025F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(    #30
        0x107,
        (
            "#067F嘿嘿，太好了。\x01",
            "不用和他打下去了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6D")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    label("loc_1F6D")


    ChrTalk(    #31
        0x101,
        "#1016F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2042")

    ChrTalk(    #32
        0x106,
        (
            "#053F确实，既然时机未到，\x01",
            "那也只能留待到下次了。\x02\x03",

            "#552F只不过，下次再碰面的话，\x01",
            "就绝对免不了要做个了断了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2024")
    TurnDirection(0x101, 0x106, 400)
    Sleep(300)

    label("loc_2024")


    ChrTalk(    #33
        0x101,
        "#1003F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_2042")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F1")

    ChrTalk(    #34
        0x103,
        (
            "#026F既然时机未到，\x01",
            "也只能继续等待下去了。\x02\x03",

            "#022F只不过，下次再碰头的话\x01",
            "就绝对免不了要做个了断了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D3")
    TurnDirection(0x101, 0x103, 400)
    Sleep(300)

    label("loc_20D3")


    ChrTalk(    #35
        0x101,
        "#1003F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_20F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218C")

    ChrTalk(    #36
        0x105,
        (
            "#1167F既然因缘未尽，决斗\x01",
            "总是不可避免的……\x02\x03",

            "#1168F至少现在\x01",
            "不用决战，真是万幸。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216E")
    TurnDirection(0x101, 0x105, 400)
    Sleep(300)

    label("loc_216E")


    ChrTalk(    #37
        0x101,
        "#1016F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_218C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(    #38
        0x104,
        (
            "#034F哎呀呀，真想看看他和金先生\x01",
            "一决胜负啊……\x02\x03",

            "#030F不过，就期待\x01",
            "下次机会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2207")
    TurnDirection(0x101, 0x104, 400)
    Sleep(300)

    label("loc_2207")


    ChrTalk(    #39
        0x101,
        (
            "#1004F#5P下次机会……\x02\x03",

            "#1019F这件事结束之后\x01",
            "你就要变回皇子殿下了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x104,
        "#031F哎呀，你在说什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_2273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231B")

    ChrTalk(    #41
        0x109,
        (
            "#1062F不过，为了一个女人，\x01",
            "两个男人之间展开热战……\x02\x03",

            "#1061F真是浪漫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E7")
    TurnDirection(0x101, 0x109, 400)
    Sleep(300)

    label("loc_22E7")


    ChrTalk(    #42
        0x101,
        (
            "#1016F#5P嗯～虽说和雾香小姐\x01",
            "并没有直接关系……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231B")


    ChrTalk(    #43
        0x102,
        (
            "#1040F……不过，这下总算\x01",
            "可以继续前进了。\x02\x03",

            "赶快启动那里的终端\x01",
            "解除锁定吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #44
        0x101,
        "#1006F#5P嗯，就这么办！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2234)
    OP_28(0x9F, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_11_151B end

    def Function_12_239B(): pass

    label("Function_12_239B")

    Sleep(400)
    OP_24(0x77, 0x5F)
    OP_24(0x135, 0x5F)
    Sleep(400)
    OP_24(0x77, 0x5A)
    OP_24(0x135, 0x5A)
    Sleep(400)
    OP_24(0x77, 0x55)
    OP_24(0x135, 0x55)
    Sleep(400)
    OP_24(0x77, 0x50)
    OP_24(0x135, 0x50)
    Sleep(400)
    OP_24(0x77, 0x4B)
    OP_24(0x135, 0x4B)
    Sleep(400)
    OP_24(0x77, 0x46)
    OP_24(0x135, 0x46)
    Sleep(400)
    OP_24(0x77, 0x3C)
    OP_24(0x135, 0x3C)
    Sleep(400)
    OP_24(0x77, 0x32)
    OP_24(0x135, 0x32)
    Sleep(400)
    OP_24(0x77, 0x28)
    OP_24(0x135, 0x28)
    Sleep(400)
    OP_24(0x77, 0x1E)
    OP_24(0x135, 0x1E)
    Sleep(400)
    OP_23(0x77)
    OP_23(0x135)
    Return()

    # Function_12_239B end

    def Function_13_2429(): pass

    label("Function_13_2429")


    def lambda_242F():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242F)
    Sleep(80)

    def lambda_244F():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_244F)
    Sleep(100)

    def lambda_246F():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_246F)
    Sleep(150)
    OP_8E(0xF9, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
    Return()

    # Function_13_2429 end

    def Function_14_249E(): pass

    label("Function_14_249E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_14_249E")

    label("loc_24B3")

    Return()

    # Function_14_249E end

    def Function_15_24B4(): pass

    label("Function_15_24B4")


    def lambda_24BA():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24BA)

    def lambda_24D5():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_24D5)
    Sleep(500)

    def lambda_24F5():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24F5)

    def lambda_2510():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2510)
    Sleep(500)

    def lambda_2530():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2530)

    def lambda_254B():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_254B)
    Sleep(400)

    def lambda_256B():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_256B)

    def lambda_2586():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2586)
    Sleep(300)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x8, 0x1)

    def lambda_25B0():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25B0)

    def lambda_25CB():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_25CB)
    Sleep(200)

    def lambda_25EB():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_25EB)

    def lambda_2606():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2606)
    Sleep(100)

    def lambda_2626():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2626)

    def lambda_2641():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2641)
    Sleep(100)

    def lambda_2661():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2661)

    def lambda_267C():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_267C)
    Return()

    # Function_15_24B4 end

    def Function_16_2692(): pass

    label("Function_16_2692")

    OP_8E(0xFE, 0xFFFFB6FE, 0x0, 0x3138, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_2692 end

    def Function_17_26AE(): pass

    label("Function_17_26AE")

    OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0x3214, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_26AE end

    def Function_18_26CA(): pass

    label("Function_18_26CA")

    OP_8E(0xFE, 0xFFFFB82A, 0x0, 0x2B5C, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_26CA end

    def Function_19_26E6(): pass

    label("Function_19_26E6")

    OP_8E(0xFE, 0xFFFFBE10, 0x0, 0x2BA2, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_26E6 end

    def Function_20_2702(): pass

    label("Function_20_2702")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 5)
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23580, 0, -420, 270)
    SetChrPos(0x102, 23550, 0, 850, 270)
    SetChrPos(0xF8, 24710, 0, -660, 270)
    SetChrPos(0xF9, 24630, 0, 720, 270)

    def lambda_2799():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2799)

    def lambda_27A9():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27A9)
    Sleep(80)

    def lambda_27C9():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27C9)
    Sleep(100)

    def lambda_27E9():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_27E9)
    Sleep(150)

    def lambda_2809():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2809)
    FadeToBright(1000, 0)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #45
        0x8,
        "男人的声音",
        (
            "呼呼……\x01",
            "我都等得不耐烦啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2946")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2905")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2943")

    label("loc_2905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2943")

    label("loc_292C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2943")

    Jump("loc_29AB")

    label("loc_2946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296D")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29AB")

    label("loc_296D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2994")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29AB")

    label("loc_2994")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_29AB")

    Sleep(500)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_29BD():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29BD)

    def lambda_29D5():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29D5)

    def lambda_29ED():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29ED)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #46
        0x101,
        "#1005F#1P墨镜男！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1042F『瘦狼』吗……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 17480, 0, -710, 270)
    SetChrPos(0x102, 17440, 0, 930, 270)
    SetChrPos(0x108, 16010, 0, 200, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A86")
    SetChrPos(0xF9, 18670, 0, 90, 270)
    Jump("loc_2A97")

    label("loc_2A86")

    SetChrPos(0xF8, 18670, 0, 90, 270)

    label("loc_2A97")


    def lambda_2A9D():
        OP_8E(0xFE, 0xFFFFD8AA, 0x0, 0xD2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A9D)

    def lambda_2AB8():
        OP_6D(-13930, 0, 1180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AB8)

    def lambda_2AD0():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AD0)

    def lambda_2AE8():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AE8)

    def lambda_2AF8():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2AF8)
    Sleep(50)

    def lambda_2B0D():
        OP_8E(0xFE, 0xFFFFDE04, 0x0, 0xFFFFFB50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B0D)
    Sleep(100)

    def lambda_2B2D():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B2D)
    Sleep(40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B72")

    def lambda_2B5A():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFE66, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2B5A)
    Jump("loc_2B8D")

    label("loc_2B72")


    def lambda_2B78():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFE66, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2B78)

    label("loc_2B8D")

    WaitChrThread(0x102, 0x2)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC0")
    SetChrChipByIndex(0xF9, 8)
    Jump("loc_2BC5")

    label("loc_2BC0")

    SetChrChipByIndex(0xF8, 8)

    label("loc_2BC5")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x108,
        "#572F……#6P瓦鲁特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#251F#5P呼呼……终于来了啊。\x02\x03",

            "既然来到这里，\x01",
            "想必已经做好了心理准备吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x108,
        (
            "#074F#6P嗯……\x01",
            "从师父那里继承的『活人』之拳…\x02\x03",

            "#072F为了粉碎你的邪拳，\x01",
            "我会发挥出它的全部精髓的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#257F#5P……呼呼…………\x02\x03",

            "看来老头子\x01",
            "的预料果然应验了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x108,
        (
            "#073F#6P师父的……预料！？\x02\x03",

            "#076F什么意思，瓦鲁特！\x02\x03",

            "你和师父的决斗\x01",
            "果然和我有关吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#253F#5P哈哈……所以我不是说过了吗。\x02\x03",

            "要想知道这些的话\x01",
            "就先打败我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(200)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_99(0x8, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, -33300, 6900, 2900, 90)
    OP_43(0xA, 0x3, 0x0, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 2)
    SetChrPos(0xB, -33300, 6900, -2900, 90)
    OP_43(0xB, 0x3, 0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2E43():
        OP_6D(-31560, 5700, 0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E43)

    def lambda_2E5B():
        OP_67(0, 6700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E5B)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrPos(0x108, -9000, 0, 210, 270)
    SetChrPos(0x101, -7300, 0, -770, 270)
    SetChrPos(0x102, -7300, 0, 1190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECB")
    SetChrPos(0xF9, -5040, 0, 240, 270)
    Jump("loc_2EDC")

    label("loc_2ECB")

    SetChrPos(0xF8, -5040, 0, 240, 270)

    label("loc_2EDC")

    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_43(0xA, 0x0, 0x0, 0x9)
    Sleep(100)

    def lambda_2EF8():
        OP_6D(-13900, 500, 410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EF8)

    def lambda_2F10():
        OP_67(0, 3000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F10)

    def lambda_2F28():
        OP_6E(288, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F28)

    def lambda_2F38():
        OP_6B(3670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F38)
    Sleep(100)
    OP_43(0xB, 0x0, 0x0, 0xA)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xB, 0x0)
    Fade(500)

    def lambda_2F63():
        OP_6C(270000, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F63)
    OP_71(0x0, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #54
        0x8,
        (
            "#257F那种软弱无用的拳法，\x01",
            "我会在此地将其彻底埋葬……\x02\x03",

            "#253F来，决一死战吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FCF():
        OP_6D(-13930, 500, 410, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FCF)

    def lambda_2FE7():
        OP_67(0, 2920, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FE7)

    def lambda_2FFF():
        OP_6B(3000, 250)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2FFF)
    SetChrChipByIndex(0x108, 20)
    SetChrFlags(0x108, 0x1000)

    def lambda_3019():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_3019)
    Sleep(30)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 2)

    def lambda_3048():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x15E, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3048)
    OP_44(0xA, 0x3)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1000)

    def lambda_307E():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_307E)

    def lambda_308E():
        OP_91(0xFE, 0x1388, 0x0, 0x7D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_308E)

    def lambda_30A9():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30A9)

    def lambda_30C4():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_30C4)
    Sleep(30)
    OP_44(0xB, 0x3)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)

    def lambda_30FC():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_30FC)

    def lambda_310C():
        OP_91(0xFE, 0x1388, 0x0, 0xFFFFF830, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_310C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3151")
    SetChrChipByIndex(0xF9, 8)

    def lambda_3139():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_3139)
    Jump("loc_3171")

    label("loc_3151")

    SetChrChipByIndex(0xF8, 8)

    def lambda_315C():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_315C)

    label("loc_3171")

    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x461, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 21)
    Return()

    # Function_20_2702 end

    def Function_21_31A4(): pass

    label("Function_21_31A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_44(0xB, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    Call(0, 5)
    OP_6D(-19390, 0, 1250, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(6360, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_6D(-6100, 0, 720, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(7340, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, -18090, 0, -3270, 0)
    SetChrPos(0x108, -18090, 0, 3750, 180)
    SetChrPos(0x101, -10300, 0, -600, 270)
    SetChrPos(0x102, -10400, 0, 800, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32BE")
    SetChrPos(0xF9, -9200, 0, 0, 270)
    Jump("loc_32CF")

    label("loc_32BE")

    SetChrPos(0xF8, -9200, 0, 0, 270)

    label("loc_32CF")

    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    LoadEffect(0x0, "scraft\\sc007_12.eff")
    LoadEffect(0x1, "scraft\\sc007_17.eff")
    StopSound(0x11170, 0x41EB0, 0x0)
    FadeToBright(1000, 0)

    def lambda_3349():
        OP_6D(-19390, 0, 1500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3349)
    OP_67(0, 5210, -10000, 3000)
    OP_0D()
    Fade(500)
    StopSound(0x11170, 0x29810, 0x0)
    OP_6B(4270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x8,
        (
            "#259F#6P这……\x02\x03",

            "你这家伙……什么时候\x01",
            "练就了这等功夫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x108,
        (
            "#074F瓦鲁特……\x01",
            "你确实是个天才。\x02\x03",

            "但是也正因为如此，\x01",
            "导致了你疏于修练。\x02\x03",

            "#072F而所谓功夫，只有靠单调枯燥的\x01",
            "刻苦锻炼才能取得成就……\x02\x03",

            "虽然我的资质愚鲁，但经过多年苦练，\x01",
            "一样可以达到不逊于你的境界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#255F#6P………………………………………\x02\x03",

            "#257F哼哼哼……你的资质愚鲁吗？\x02\x03",

            "#253F但那老头子\x01",
            "可不是这样想啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        "#073F………哎……………\x02",
    )

    CloseMessageWindow()
    OP_1D(0x53)
    Sleep(500)

    def lambda_352E():
        OP_6B(3600, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_352E)
    Sleep(500)

    ChrTalk(    #59
        0x8,
        (
            "#253F老头子曾和我说过。\x02\x03",

            "抛开活人、杀人的理念不谈……\x02\x03",

            "单论资质和才能……\x01",
            "你统统都在我之上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x108,
        "#076F什…什么…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#253F#6P而老头子又打算让更有才能的弟子\x01",
            "继承『泰斗流』。\x02\x03",

            "……这话的含义，\x01",
            "就算你再迟钝也能明白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x108,
        (
            "#075F但、但是……\x02\x03",

            "#072F说我比你有资质\x01",
            "开玩笑也要看场合吧！？\x02\x03",

            "而且师父，也不可能\x01",
            "不顾及雾香的感情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#250F……呼呼呼……\x01",
            "所以说你这家伙头脑真简单。\x02\x03",

            "失去了流派的继承权，\x01",
            "却还厚着脸皮和师父的女儿在一起……\x02\x03",

            "那种事……\x01",
            "你以为我能接受吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        "#572F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#251F所以我向老头子提出请求，\x01",
            "想以和你决胜负的方式来决定继承权的归属。\x02\x03",

            "但是，老头子他却这么说。\x02\x03",

            "#257F『──金会在无意识中\x01",
            "对你容让留情』\x02\x03",

            "『无论武术，还是女人』\x02\x03",

            "#255F『如果你总是现在这个样子……\x01",
            "那他的武术就永远无法取得大成』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x108,
        "#073F…………什……什么…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#253F#6P呼呼……我当时年轻气盛，\x01",
            "听了这种话之后，更加接受不了。\x02\x03",

            "而老头子提出…代替你\x01",
            "和我决一死战……\x02\x03",

            "#257F结果我──战胜了老头子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        "#072F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#253F#6P呼呼呼……这就是\x01",
            "我和老头子死斗的理由。\x02\x03",

            "如你所愿，我把一切都告诉你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x108,
        (
            "#074F……………………………………\x02\x03",

            "我一直想知道……\x02\x03",

            "师父当年为何要\x01",
            "向你提出决斗……\x02\x03",

            "#572F如今终于……明白答案了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "#255F#6P……什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        (
            "#072F瓦鲁特……\x01",
            "其实你误会了。\x02\x03",

            "我也是之后\x01",
            "才从雾香那里得知……\x02\x03",

            "#074F在当时，龙牙师父\x01",
            "似乎就已经身患重病了。\x02\x03",

            "听说是恶性肿瘤。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x8,
        "#258F#6P……什…什么…！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x108,
        (
            "#072F正因如此，师父\x01",
            "才向你提出决战的要求。\x02\x03",

            "目的当然是想亲身告诉你什么是\x01",
            "武术的真正含义……\x02\x03",

            "同时也打算对未成熟的我\x01",
            "显示武术的极致吧。\x02\x03",

            "#572F然而，师父最大的愿望……\x02\x03",

            "#074F就是将武术家的生命\x01",
            "在与第一号弟子的战斗中\x01",
            "结束掉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#254F#6P……………………………………\x02\x03",

            "#252F……呼呼……那算什么……\x02\x03",

            "那种蠢话……\x01",
            "……怎么可能……\x02\x03",

            "那就是说，\x01",
            "我只是被老头子利用了而已吗？\x02\x03",

            "如果是那样的话……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x108,
        (
            "#074F的确……\x01",
            "师傅的做法也许有些自作主张。\x02\x03",

            "#072F但是，习武者追求最强境界\x01",
            "的信念，本身不也是出于利己的想法吗。\x02\x03",

            "这也许正是我们武术家\x01",
            "所必须背负的宿命也说不定。\x02\x03",

            "#572F所以师父……\x01",
            "才会如此武断地做出决定。\x02\x03",

            "用这种极端的方式，让你我二人\x01",
            "感受到武术的光与暗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#254F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x108, 21)
    OP_0D()
    Sleep(500)

    ChrTalk(    #78
        0x108,
        "#072F……瓦鲁特，接招吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#255F#6P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x108,
        (
            "#072F我要把从师傅和你身上学到，\x01",
            "并在游击士职业中磨练而成的\x01",
            "『泰斗』精华，全部都寄托在这一拳上。\x02\x03",

            "这一拳，要把你这个堕入修罗道的\x01",
            "不成器师兄彻底打醒。\x02\x03",

            "#074F这或许也是我这个当师弟的\x01",
            "能为你做的最后一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#255F#6P……………………………………\x02\x03",

            "#257F……哼…………\x01",
            "真能吹牛啊………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #82
        0x8,
        (
            "#253F那我就将在结社中磨练出来的\x01",
            "全部秘技凝集在这一拳中……\x02\x03",

            "将『泰斗』的一切彻底埋葬！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    Fade(500)
    OP_6D(-19320, 0, 0, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -8300, 0, -600, 270)
    SetChrPos(0x102, -8400, 0, 800, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FFC")
    SetChrPos(0xF9, -7200, 0, 0, 270)
    Jump("loc_400D")

    label("loc_3FFC")

    SetChrPos(0xF8, -7200, 0, 0, 270)

    label("loc_400D")

    OP_71(0x0, 0x4)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #83
        0x108,
        "#072F#4P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "#255F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 12)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 16)
    OP_0D()

    def lambda_40FB():
        OP_99(0xFE, 0x0, 0x7, 0x708)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_40FB)

    def lambda_410B():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_410B)
    WaitChrThread(0x8, 0x1)
    Sleep(700)

    def lambda_4125():

        label("loc_4125")

        OP_7C(0x64, 0x0, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_4125")

    QueueWorkItem2(0x101, 3, lambda_4125)
    OP_22(0x85, 0x0, 0x64)

    ChrTalk(    #85
        0x108,
        "#077F#1K#4P嗬啊啊啊啊啊啊啊啊啊……！\x02",
    )


    ChrTalk(    #86
        0x8,
        "#259F#1K#1P唔哦哦哦哦哦哦哦哦哦……！\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(1000)
    OP_6D(-13000, 0, 0, 1500)
    Sleep(500)

    ChrTalk(    #87
        0x101,
        "#1020F#6P（好、好厉害……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#1043F#4P（这样下去必有一方……）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-19320, 0, 0, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_4247():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4247)

    ChrTalk(    #89 op#A op#5
        0x108,
        "#076F#4P#30A哦哦哦哦哦哦哦哦哦哦哦哦……！\x05\x02",
    )


    ChrTalk(    #90 op#A op#5
        0x8,
        "#258F#1P#30A啊啊啊啊啊啊啊啊啊啊啊啊……！\x05\x02",
    )

    Sleep(5000)
    OP_56(0x0)
    WaitChrThread(0x101, 0x2)

    def lambda_42C3():
        OP_6B(3000, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42C3)
    OP_44(0x101, 0x3)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_23(0x85)
    SetChrFlags(0x108, 0x20)
    SetChrFlags(0x108, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x40)
    OP_7D(0x0, 0x108, 0x32, 0x1F4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_4304():
        OP_8E(0xFE, 0xFFFFB956, 0x0, 0xEA6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4304)

    def lambda_431F():
        OP_8E(0xFE, 0xFFFFB956, 0x0, 0xFFFFF33A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_431F)
    SetChrChipByIndex(0x108, 10)
    SetChrSubChip(0x108, 3)
    SetChrChipByIndex(0x8, 17)
    SetChrSubChip(0x8, 1)
    PlayEffect(0x1, 0x0, 0xFF, -18090, 800, 240, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
    FadeToDark(100, 16777215, -1)
    WaitChrThread(0x108, 0x1)
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x40)
    OP_7D(0x1, 0x108, 0x0, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(-19390, 0, 1500, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x4)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(2000)

    ChrTalk(    #91
        0x8,
        "#254F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x108,
        (
            "#074F#6P……………………………………\x02\x03",

            "#572F……………唔…………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 11)
    OP_99(0x108, 0x0, 0x1, 0x4B0)

    def lambda_44B4():
        OP_6D(-19390, 0, -500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44B4)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x108, 0x1, 0x3, 0x4B0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #93
        0x102,
        "#1044F#1P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1020F#1P金，金先生！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 1)
    OP_0D()
    OP_8C(0x8, 180, 400)
    SetChrPos(0x8, -18090, 0, 3500, 180)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)

    ChrTalk(    #95
        0x8,
        (
            "#253F#6P#40W呼呼呼……\x01",
            "……真没办法……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_458F():
        OP_6D(-19390, 0, 3500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_458F)
    OP_99(0x8, 0x0, 0x4, 0x3E8)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(1000)
    OP_99(0x8, 0x4, 0x6, 0x320)
    Sleep(200)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #96
        0x8,
        (
            "#253F#2P#40W……拥有这等功夫，\x01",
            "却把它埋藏在污泥之中……\x02\x03",

            "#257F#40W呼呼……老头子的话\x01",
            "………我总算明白了………\x02\x03",

            "#250F#60W……呼……美味……\x02\x03",

            "#80W香烟……真是……\x01",
            "…………美味啊……………\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 24)
    OP_99(0x8, 0x18, 0x1E, 0x5DC)
    Sleep(200)

    def lambda_46AA():
        OP_6D(-19390, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46AA)
    SetChrSubChip(0x8, 10)
    OP_99(0x8, 0xA, 0x12, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x8, 0x13, 0x17, 0x5DC)
    Sleep(1000)
    Fade(500)
    OP_6D(-14570, 0, 810, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(3890, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_47A9")

    label("loc_476B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4792")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_47A9")

    label("loc_4792")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_47A9")

    Jump("loc_4811")

    label("loc_47AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D3")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4811")

    label("loc_47D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47FA")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4811")

    label("loc_47FA")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4811")

    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x101,
        "#1025F#6P难，难不成……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#1040F#2P嗯……\x01",
            "看来是金先生赢了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_487D():
        OP_6D(-17900, 0, -2700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_487D)

    def lambda_4895():
        OP_67(0, 5260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4895)

    def lambda_48AD():
        OP_6B(3580, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48AD)
    OP_43(0x101, 0x1, 0x0, 0x17)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x18)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E6")
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Jump("loc_48ED")

    label("loc_48E6")

    OP_43(0xF8, 0x1, 0x0, 0x1A)

    label("loc_48ED")

    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_493F")

    ChrTalk(    #99
        0x106,
        (
            "#051F嘿嘿……\x01",
            "成功了嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_493F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4971")

    ChrTalk(    #100
        0x103,
        "#021F金先生……你成功了呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_4971")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49A2")

    ChrTalk(    #101
        0x104,
        (
            "#031F呼……\x01",
            "漂亮的胜利哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_49A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D0")

    ChrTalk(    #102
        0x109,
        (
            "#1061F呀～！\x01",
            "真是厉害！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_49D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49FD")

    ChrTalk(    #103
        0x105,
        "#1168F……漂亮的胜利。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_49FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A30")

    ChrTalk(    #104
        0x107,
        (
            "#067F哇～……\x01",
            "好，好厉害……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6E")

    label("loc_4A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A6E")

    ChrTalk(    #105
        0x10B,
        (
            "#210F真、真不敢相信……\x01",
            "实在是大开眼界啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6E")


    ChrTalk(    #106
        0x101,
        (
            "#1001F#6P嗯嗯！\x02\x03",

            "#1018F真没想到！和这么厉害的人\x01",
            "正面决斗竟然还能赢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x108,
        "#074F#5P……不………\x02",
    )

    CloseMessageWindow()

    def lambda_4AD8():

        label("loc_4AD8")

        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x7D0)
        OP_48()
        Jump("loc_4AD8")

    QueueWorkItem2(0x108, 3, lambda_4AD8)
    Sleep(300)
    OP_99(0x108, 0x3, 0x0, 0x320)
    OP_44(0x108, 0x3)
    Fade(500)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0x108, 0)
    OP_0D()

    def lambda_4B17():
        OP_8C(0x102, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B17)
    Sleep(200)
    OP_8C(0x108, 90, 300)
    Sleep(500)

    ChrTalk(    #108
        0x108,
        (
            "#074F#5P我之所以能够获胜，只是因为\x01",
            "我背负着『泰斗流』之名而战。\x02\x03",

            "#572F如果那家伙\x01",
            "也使用正宗的『泰斗』武术\x01",
            "来应战的话……\x02\x03",

            "倒下的\x01",
            "大概会是我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1016F#6P真是的～没那种事啦。\x02\x03",

            "#1015F对了金先生……\x01",
            "有没有受伤？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#1044F需要治疗一下吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#074F#5P不……没问题。\x02\x03",

            "#070F……瓦鲁特那家伙\x01",
            "暂时还不会醒来，\x01",
            "就放他在这里也没关系吧。\x02\x03",

            "现在我们赶快往上走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1006F#6P……嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        (
            "#1040F那么，\x01",
            "去操纵那里的终端吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17410, 0, 4440, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 23)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A2(0x2235)
    OP_28(0x9F, 0x1, 0x20)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x0)
    OP_1D(0x40)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_31A4 end

    def Function_22_4D41(): pass

    label("Function_22_4D41")


    def lambda_4D47():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D47)
    Sleep(40)

    def lambda_4D67():
        OP_8E(0xFE, 0x448E, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4D67)
    Sleep(100)

    def lambda_4D87():
        OP_8E(0xFE, 0x4916, 0x0, 0x4F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D87)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC5")
    OP_8E(0xF9, 0x48C6, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)
    Jump("loc_4DD9")

    label("loc_4DC5")

    OP_8E(0xF8, 0x48C6, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)

    label("loc_4DD9")

    Return()

    # Function_22_4D41 end

    def Function_23_4DDA(): pass

    label("Function_23_4DDA")

    OP_8E(0xFE, 0xFFFFC00E, 0x0, 0xFFFFEF8E, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_4DDA end

    def Function_24_4DF6(): pass

    label("Function_24_4DF6")

    OP_8E(0xFE, 0xFFFFBF6E, 0x0, 0xFFFFF452, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_4DF6 end

    def Function_25_4E12(): pass

    label("Function_25_4E12")

    OP_8E(0xFE, 0xFFFFC428, 0x0, 0xFFFFF150, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_4E12 end

    def Function_26_4E2E(): pass

    label("Function_26_4E2E")

    OP_8E(0xFE, 0xFFFFC428, 0x0, 0xFFFFF150, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_26_4E2E end

    def Function_27_4E4A(): pass

    label("Function_27_4E4A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #114
        (
            "\x07\x05向上层区域方向的隔离壁，\x01",
            "以及传送门的锁定解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5303   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_27_4E4A end

    def Function_28_4EB6(): pass

    label("Function_28_4EB6")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ECD")
    Call(0, 30)
    Call(0, 31)

    label("loc_4ECD")

    OP_6D(-33350, 0, 660, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -31400, 0, -720, 270)
    SetChrPos(0x102, -31400, 0, 210, 270)
    SetChrPos(0xF8, -29800, 0, -1260, 270)
    SetChrPos(0xF9, -29800, 0, 10, 270)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声音")

    AnonymousTalk(    #115
        (
            "\x07\x05向上层区域方向的隔离壁，\x01",
            "以及传送门的锁定已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_71(0x1, 0x4)
    OP_0D()
    Sleep(500)
    OP_64(0x0, 0x1)
    OP_A2(0x2236)
    OP_28(0x9F, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_28_4EB6 end

    def Function_29_4FCD(): pass

    label("Function_29_4FCD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FE4")
    Call(0, 30)
    Call(0, 31)

    label("loc_4FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF9")
    Call(0, 6)
    Jump("loc_4FFD")

    label("loc_4FF9")

    Call(0, 20)

    label("loc_4FFD")

    Return()

    # Function_29_4FCD end

    def Function_30_4FFE(): pass

    label("Function_30_4FFE")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5078"),
        (1, "loc_507E"),
        (SWITCH_DEFAULT, "loc_5084"),
    )


    label("loc_5078")

    OP_A2(0x1200)
    Jump("loc_5084")

    label("loc_507E")

    OP_A2(0x1201)
    Jump("loc_5084")

    label("loc_5084")

    Return()

    # Function_30_4FFE end

    def Function_31_5085(): pass

    label("Function_31_5085")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_31_5085 end

    def Function_32_5118(): pass

    label("Function_32_5118")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_32_5118 end

    SaveToFile()

Try(main)
