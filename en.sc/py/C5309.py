from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Walter',                               # 9
        'Walter',                               # 10
        'ブラッドクーガー',                     # 11
        'ブラッドクーガー',                     # 12
        'Pale Apache',                          # 13
        '幻惑のルシオラ',                       # 14
        'Targeting Camera',                     # 15
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
        "Function_4_4FE",          # 04, 4
        "Function_5_779",          # 05, 5
        "Function_6_A68",          # 06, 6
        "Function_7_1427",         # 07, 7
        "Function_8_14A7",         # 08, 8
        "Function_9_1527",         # 09, 9
        "Function_10_15D4",        # 0A, 10
        "Function_11_1681",        # 0B, 11
        "Function_12_2A86",        # 0C, 12
        "Function_13_2B14",        # 0D, 13
        "Function_14_2B89",        # 0E, 14
        "Function_15_2B9F",        # 0F, 15
        "Function_16_2D7D",        # 10, 16
        "Function_17_2D99",        # 11, 17
        "Function_18_2DB5",        # 12, 18
        "Function_19_2DD1",        # 13, 19
        "Function_20_2DED",        # 14, 20
        "Function_21_3956",        # 15, 21
        "Function_22_58F8",        # 16, 22
        "Function_23_5991",        # 17, 23
        "Function_24_59AD",        # 18, 24
        "Function_25_59C9",        # 19, 25
        "Function_26_59E5",        # 1A, 26
        "Function_27_5A01",        # 1B, 27
        "Function_28_5A77",        # 1C, 28
        "Function_29_5B92",        # 1D, 29
        "Function_30_5BC3",        # 1E, 30
        "Function_31_5C49",        # 1F, 31
        "Function_32_5CDC",        # 20, 32
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
        "#5P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Walter is unconscious, unable to move.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_494 end

    def Function_4_4FE(): pass

    label("Function_4_4FE")

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
        (2, "loc_585"),
        (5, "loc_59C"),
        (3, "loc_5B3"),
        (4, "loc_5CA"),
        (6, "loc_5E1"),
        (8, "loc_5F8"),
        (10, "loc_60F"),
        (14, "loc_626"),
        (15, "loc_63D"),
        (SWITCH_DEFAULT, "loc_654"),
    )


    label("loc_585")

    OP_D2(0x701D0, 0x701DC, 0xA)
    OP_D2(0x701D1, 0x701DD, 0xB)
    Jump("loc_654")

    label("loc_59C")

    OP_D2(0x70218, 0x70224, 0xA)
    OP_D2(0x70219, 0x70225, 0xB)
    Jump("loc_654")

    label("loc_5B3")

    OP_D2(0x701E8, 0x701F4, 0xA)
    OP_D2(0x701E9, 0x701F5, 0xB)
    Jump("loc_654")

    label("loc_5CA")

    OP_D2(0x27036E, 0x27037B, 0xA)
    OP_D2(0x27036F, 0x27037C, 0xB)
    Jump("loc_654")

    label("loc_5E1")

    OP_D2(0x70230, 0x7023C, 0xA)
    OP_D2(0x70231, 0x7023D, 0xB)
    Jump("loc_654")

    label("loc_5F8")

    OP_D2(0x270176, 0x270183, 0xA)
    OP_D2(0x270177, 0x270184, 0xB)
    Jump("loc_654")

    label("loc_60F")

    OP_D2(0x702B4, 0x702BB, 0xA)
    OP_D2(0x702B5, 0x702BC, 0xB)
    Jump("loc_654")

    label("loc_626")

    OP_D2(0x2702D6, 0x2702E0, 0xA)
    OP_D2(0x2702D7, 0x2702E1, 0xB)
    Jump("loc_654")

    label("loc_63D")

    OP_D2(0x2702C2, 0x2702CC, 0xA)
    OP_D2(0x2702C3, 0x2702CD, 0xB)
    Jump("loc_654")

    label("loc_654")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_681"),
        (5, "loc_698"),
        (3, "loc_6AF"),
        (4, "loc_6C6"),
        (6, "loc_6DD"),
        (8, "loc_6F4"),
        (10, "loc_70B"),
        (14, "loc_722"),
        (15, "loc_739"),
        (SWITCH_DEFAULT, "loc_750"),
    )


    label("loc_681")

    OP_D2(0x701D0, 0x701DC, 0xC)
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_750")

    label("loc_698")

    OP_D2(0x70218, 0x70224, 0xC)
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_750")

    label("loc_6AF")

    OP_D2(0x701E8, 0x701F4, 0xC)
    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_750")

    label("loc_6C6")

    OP_D2(0x27036E, 0x27037B, 0xC)
    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_750")

    label("loc_6DD")

    OP_D2(0x70230, 0x7023C, 0xC)
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_750")

    label("loc_6F4")

    OP_D2(0x270176, 0x270183, 0xC)
    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_750")

    label("loc_70B")

    OP_D2(0x702B4, 0x702BB, 0xC)
    OP_D2(0x702B5, 0x702BC, 0xD)
    Jump("loc_750")

    label("loc_722")

    OP_D2(0x2702D6, 0x2702E0, 0xC)
    OP_D2(0x2702D7, 0x2702E1, 0xD)
    Jump("loc_750")

    label("loc_739")

    OP_D2(0x2702C2, 0x2702CC, 0xC)
    OP_D2(0x2702C3, 0x2702CD, 0xD)
    Jump("loc_750")

    label("loc_750")

    OP_D2(0x27022A, 0x270234, 0xE)
    OP_D2(0x2600A0, 0x2600A5, 0xF)
    OP_D2(0x260052, 0x260057, 0x10)
    OP_D2(0x2601C4, 0x2601C9, 0x11)
    Return()

    # Function_4_4FE end

    def Function_5_779(): pass

    label("Function_5_779")

    OP_D2(0x2701C6, 0x2701CB, 0x1)
    OP_D2(0x290428, 0x29042C, 0x2)
    OP_D2(0x290429, 0x29042D, 0x3)
    OP_D2(0x270110, 0x270120, 0x4)
    OP_D2(0x270111, 0x270121, 0x5)
    OP_D2(0x270130, 0x270140, 0x6)
    OP_D2(0x270131, 0x270141, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E4")
    OP_D2(0x701D0, 0x701DC, 0x8)
    OP_D2(0x701D1, 0x701DD, 0x9)
    Jump("loc_909")

    label("loc_7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_809")
    OP_D2(0x70218, 0x70224, 0x8)
    OP_D2(0x70219, 0x70225, 0x9)
    Jump("loc_909")

    label("loc_809")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E")
    OP_D2(0x701E8, 0x701F4, 0x8)
    OP_D2(0x701E9, 0x701F5, 0x9)
    Jump("loc_909")

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_853")
    OP_D2(0x27036E, 0x27037B, 0x8)
    OP_D2(0x27036F, 0x27037C, 0x9)
    Jump("loc_909")

    label("loc_853")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_878")
    OP_D2(0x70230, 0x7023C, 0x8)
    OP_D2(0x70231, 0x7023D, 0x9)
    Jump("loc_909")

    label("loc_878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")
    OP_D2(0x270176, 0x270183, 0x8)
    OP_D2(0x270177, 0x270184, 0x9)
    Jump("loc_909")

    label("loc_89D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C2")
    OP_D2(0x702B4, 0x702BB, 0x8)
    OP_D2(0x702B5, 0x702BC, 0x9)
    Jump("loc_909")

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E7")
    OP_D2(0x2702D6, 0x2702E0, 0x8)
    OP_D2(0x2702D7, 0x2702E1, 0x9)
    Jump("loc_909")

    label("loc_8E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_909")
    OP_D2(0x2702C2, 0x2702CC, 0x8)
    OP_D2(0x2702C3, 0x2702CD, 0x9)

    label("loc_909")

    OP_D2(0x7024A, 0x70256, 0xA)
    OP_D2(0x7024C, 0x70258, 0xB)
    OP_D2(0x70251, 0x7025D, 0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_942")
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_A17")

    label("loc_942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D")
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_A17")

    label("loc_95D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_978")
    OP_D2(0x701E9, 0x701F5, 0xD)
    Jump("loc_A17")

    label("loc_978")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_993")
    OP_D2(0x27036F, 0x27037C, 0xD)
    Jump("loc_A17")

    label("loc_993")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AE")
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_A17")

    label("loc_9AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C9")
    OP_D2(0x270177, 0x270184, 0xD)
    Jump("loc_A17")

    label("loc_9C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E4")
    OP_D2(0x702B5, 0x702BC, 0xD)
    Jump("loc_A17")

    label("loc_9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FF")
    OP_D2(0x2702D7, 0x2702E1, 0x9)
    Jump("loc_A17")

    label("loc_9FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A17")
    OP_D2(0x2702C3, 0x2702CD, 0x9)

    label("loc_A17")

    OP_D2(0x27022A, 0x270234, 0xE)
    OP_D2(0x2600A0, 0x2600A5, 0xF)
    OP_D2(0x2601A7, 0x2601AC, 0x10)
    OP_D2(0x27022C, 0x270236, 0x11)
    OP_D2(0x2601C5, 0x2601CA, 0x12)
    OP_D2(0x260052, 0x260057, 0x13)
    OP_D2(0x70249, 0x70255, 0x14)
    OP_D2(0x70248, 0x70254, 0x15)
    Return()

    # Function_5_779 end

    def Function_6_A68(): pass

    label("Function_6_A68")

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

    def lambda_AFF():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFF)

    def lambda_B0F():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0F)
    Sleep(80)

    def lambda_B2F():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2F)
    Sleep(100)

    def lambda_B4F():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B4F)
    Sleep(150)

    def lambda_B6F():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B6F)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #2
        0x8,
        "Man's Voice",
        "About goddamn time.\x02",
    )

    CloseMessageWindow()
    OP_20(0x1F4)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3B")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C79")

    label("loc_C3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C62")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C79")

    label("loc_C62")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C79")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CE3")

    label("loc_CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CE3")

    label("loc_CCC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CE3")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D05")

    ChrTalk(    #3
        0x110,
        "#270FHmm?\x02",
    )

    CloseMessageWindow()

    label("loc_D05")

    OP_1D(0x6F)
    Sleep(500)

    def lambda_D12():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D12)

    def lambda_D2A():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D2A)

    def lambda_D42():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D42)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x101,
        "#1005F#1PWalter the Direwolf!\x02",
    )

    CloseMessageWindow()

    def lambda_D7F():
        OP_8E(0xFE, 0xFFFFDCEC, 0x0, 0xFFFFFE3E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7F)

    def lambda_D9A():
        OP_6D(-14650, 0, 2440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D9A)

    def lambda_DB2():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DB2)

    def lambda_DCA():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DCA)

    def lambda_DDA():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_DDA)
    Sleep(300)

    def lambda_DEF():
        OP_8E(0xFE, 0xFFFFDD82, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DEF)
    Sleep(100)

    def lambda_E0F():
        OP_8E(0xFE, 0xFFFFE46C, 0x0, 0xFFFFFBB4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_E0F)
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

    ChrTalk(    #5
        0x102,
        "#1042F#2PWalter... So you'll be up next.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#254F#6PI guess I'm somethin' like an\x01",
            "obstacle, yeah.\x02\x03",

            "More importantly, kids, ain't Zin\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1035F#2PHe's currently on standby aboard\x01",
            "the Arseille.\x02\x03",

            "#1042FI'm afraid you misjudged if you\x01",
            "thought he would be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "#254F#6PTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F#2PUh... If you'd like, we can give\x01",
            "him a message.\x02\x03",

            "We can take one to Kilika, too, if you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#250F#6PDon't even try bein' thoughtful.\x02\x03",

            "Ah, well. No use gettin' angry if\x01",
            "he's not here.\x02\x03",

            "Let's just get this over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1002F#2PAll right.\x02",
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

    def lambda_1113():
        OP_6D(-31560, 5700, 0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1113)

    def lambda_112B():
        OP_67(0, 6700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_112B)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrPos(0x101, -9130, 0, -310, 270)
    SetChrPos(0x102, -9130, 0, 1050, 270)
    SetChrPos(0xF8, -6990, 0, -720, 270)
    SetChrPos(0xF9, -6990, 0, 1490, 270)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_43(0xA, 0x0, 0x0, 0x9)
    Sleep(100)

    def lambda_11B5():
        OP_6D(-13900, 500, 410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11B5)

    def lambda_11CD():
        OP_67(0, 3000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11CD)

    def lambda_11E5():
        OP_6E(288, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11E5)

    def lambda_11F5():
        OP_6B(3670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11F5)
    Sleep(100)
    OP_43(0xB, 0x0, 0x0, 0xA)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xB, 0x0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)

    def lambda_122E():
        OP_6C(270000, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_122E)
    OP_71(0x0, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #12
        0x8,
        (
            "#252F#6PHere we go.\x02\x03",

            "Hope you can put up half the\x01",
            "fight Zin would!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1291():
        OP_6D(-13930, 500, 410, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1291)

    def lambda_12A9():
        OP_67(0, 2800, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12A9)

    def lambda_12C1():
        OP_6B(3000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12C1)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x8, 16)

    def lambda_12E0():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x15E, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_12E0)
    Sleep(30)
    OP_44(0xA, 0x3)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1000)

    def lambda_131B():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_131B)

    def lambda_132B():
        OP_91(0xFE, 0x1388, 0x0, 0x7D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_132B)

    def lambda_1346():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1346)

    def lambda_1361():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1361)
    Sleep(30)
    OP_44(0xB, 0x3)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)

    def lambda_1399():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1399)

    def lambda_13A9():
        OP_91(0xFE, 0x1388, 0x0, 0xFFFFF830, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_13A9)

    def lambda_13C4():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_13C4)

    def lambda_13DF():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_13DF)
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

    # Function_6_A68 end

    def Function_7_1427(): pass

    label("Function_7_1427")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -18950, 1800, -1850, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1458():

        label("loc_1458")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1458")

    QueueWorkItem2(0xFE, 1, lambda_1458)

    def lambda_146B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_146B)

    def lambda_147D():
        OP_8F(0xFE, 0xFFFFB5FA, 0x1F4, 0xFFFFF8C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_147D)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_7_1427 end

    def Function_8_14A7(): pass

    label("Function_8_14A7")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 2)
    SetChrPos(0xFE, -18950, 1800, 1850, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_14D8():

        label("loc_14D8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14D8")

    QueueWorkItem2(0xFE, 1, lambda_14D8)

    def lambda_14EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14EB)

    def lambda_14FD():
        OP_8F(0xFE, 0xFFFFB5FA, 0x1F4, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_14FD)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_8_14A7 end

    def Function_9_1527(): pass

    label("Function_9_1527")

    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 135, 0)
    ClearChrFlags(0xFE, 0x800)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_154C():
        OP_99(0xFE, 0x5, 0x7, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_154C)

    def lambda_155C():
        OP_96(0xFE, 0xFFFFAD6C, 0x0, 0xFFFFEB4C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_155C)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 45, 0)

    def lambda_158B():
        OP_99(0xFE, 0x5, 0x7, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_158B)

    def lambda_159B():
        OP_96(0xFE, 0xFFFFBF28, 0x0, 0xFFFFF2CC, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_159B)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_9_1527 end

    def Function_10_15D4(): pass

    label("Function_10_15D4")

    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 45, 0)
    ClearChrFlags(0xFE, 0x800)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_15F9():
        OP_99(0xFE, 0x5, 0x7, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15F9)

    def lambda_1609():
        OP_96(0xFE, 0xFFFFAD6C, 0x0, 0x1694, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1609)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 135, 0)

    def lambda_1638():
        OP_99(0xFE, 0x5, 0x7, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1638)

    def lambda_1648():
        OP_96(0xFE, 0xFFFFBF28, 0x0, 0xF14, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1648)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_10_15D4 end

    def Function_11_1681(): pass

    label("Function_11_1681")

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

    ChrTalk(    #13
        0x8,
        "#254F#6PTch! Damned kids...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1019F#2POh, come on, where's this 'kids'\x01",
            "thing coming from?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188F")

    ChrTalk(    #15
        0x110,
        (
            "#277FHeh...\x02\x03",

            "You're the one who's doubled over\x01",
            "from fighting a pack of 'children.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_188F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EE")

    ChrTalk(    #16
        0x106,
        (
            "#051F#2PHeh...\x02\x03",

            "Hey, old timer. You need some\x01",
            "help stayin' on your feet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_18EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1999")

    ChrTalk(    #17
        0x10B,
        (
            "#210F#2PWell, yeah, we do have at least\x01",
            "one kid in the party.\x02\x03",

            "I'd appreciate it if you wouldn't call\x01",
            "ME what you do HER, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1022F#2PHey!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1999")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(    #19
        0x109,
        (
            "#1066F#2PC'mon, now, Estelle, don't get too grumpy.\x02\x03",

            "You're sorta piling on a guy who's CLEARLY\x01",
            "going over the hill, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AC8")

    ChrTalk(    #20
        0x104,
        (
            "#035F#2PCome now, Estelle. Have some\x01",
            "compassion.\x02\x03",

            "#030FWe must be mindful of the feelings\x01",
            "of those who are soon to be put to\x01",
            "pasture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(    #21
        0x105,
        (
            "#1162F#2PWe may be young, yes.\x02\x03",

            "But we still have strength enough\x01",
            "to protect what is dear to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BBE")

    ChrTalk(    #22
        0x103,
        (
            "#027F#2PNow, Estelle. Be nice.\x02\x03",

            "It's not kind to mock a man who has\x01",
            "clearly passed his prime, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1BBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C0A")

    ChrTalk(    #23
        0x10F,
        (
            "#176FVictory is ours.\x02\x03",

            "#178FRepent, Walter the Direwolf!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0A")


    ChrTalk(    #24
        0x8,
        "#254F#6PPffeh. Stupid shrieking birds...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1035F#2PWalter. You don't really have a reason\x01",
            "to stay, do you?\x02\x03",

            "#1042FWe, however, have many reasons to\x01",
            "keep going.\x02\x03",

            "Do you still want to fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1026F#2PJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#254F#6P...\x02\x03",

            "#251FHah... Damn but you know how to\x01",
            "turn a guy off, Fang.\x02",
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

    def lambda_1D68():
        OP_6D(-18010, 0, 6140, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D68)

    def lambda_1D80():
        OP_67(0, 6340, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D80)

    def lambda_1D98():
        OP_6B(5850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D98)

    def lambda_1DA8():
        OP_6E(307, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DA8)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E4C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E8A")

    label("loc_1E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E73")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E8A")

    label("loc_1E73")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1E8A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB6")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EF4")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1EF4")

    label("loc_1EDD")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1EF4")

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

    ChrTalk(    #28
        0x101,
        "#1020F#1PWhoa, wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#257F#6PYou wanted to carry a message?\x01",
            "Cool. Tell Zin the match is held\x01",
            "up till next time.\x02\x03",

            "#253FSo, later, kids.\x02\x03",

            "Try not to let the Faceless up there\x01",
            "eat your brains!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_209B():
        OP_6D(-17240, 5430, 12640, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_209B)

    def lambda_20B3():
        OP_67(0, 5540, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20B3)

    def lambda_20CB():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20CB)

    def lambda_20DB():
        OP_6E(274, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_20DB)
    SetChrFlags(0x8, 0x20)

    def lambda_20F0():
        OP_97(0xC, 0xFFFFABFA, 0x1090, 0xFFFEA070, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_20F0)
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

    ChrTalk(    #30
        0x101,
        "#1015F#6PHe's gone...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #31
        0x102,
        (
            "#1035F#4PHe knew that his chance to settle\x01",
            "things with Zin has passed.\x02\x03",

            "#1040FHe'll be like Bleublanc--he won't\x01",
            "trouble us again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #32
        0x101,
        "#1025F#6PCool!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(    #33
        0x10F,
        (
            "#175FBlast. I'd intended to make him pay,\x01",
            "here and now, for his crimes in the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10F, 400)

    ChrTalk(    #34
        0x101,
        (
            "#4P#1002FYeah, he did put Kloe and Her Majesty\x01",
            "in danger, and hurt a lot of people.\x02\x03",

            "#1003FBut the real criminal here is Weissmann.\x02\x03",

            "The Enforcers just responded to his\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x101, 400)

    ChrTalk(    #35
        0x10F,
        (
            "#176FTrue.\x02\x03",

            "#178FI still feel unsatisfied,\x01",
            "but we should press on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2417")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249C")

    ChrTalk(    #36
        0x107,
        (
            "#067FI'm glad we didn't have to\x01",
            "fight more, personally.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247B")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    label("loc_247B")


    ChrTalk(    #37
        0x101,
        "#1016F#6PYeah...me, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_249C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256C")

    ChrTalk(    #38
        0x106,
        (
            "#053FYeah, everything's got a time and place.\x02\x03",

            "#552FSomehow, though, I can't think they'll\x01",
            "avoid a fight the next time they meet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254A")
    TurnDirection(0x101, 0x106, 400)
    Sleep(300)

    label("loc_254A")


    ChrTalk(    #39
        0x101,
        "#1003F#6PYeah...probably.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_256C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2654")

    ChrTalk(    #40
        0x103,
        (
            "#026FYes, to everything there is a season.\x02\x03",

            "#022FWhat I'm afraid of is the fact that they\x01",
            "won't be able to avoid settling things\x01",
            "the next time they meet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2632")
    TurnDirection(0x101, 0x103, 400)
    Sleep(300)

    label("loc_2632")


    ChrTalk(    #41
        0x101,
        "#1003F#6PYeah...probably.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2725")

    ChrTalk(    #42
        0x105,
        (
            "#1167FAs long as this stands between them,\x01",
            "I fear they'll have to fight...someday.\x02\x03",

            "#1168FI'm just grateful that day was not today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2704")
    TurnDirection(0x101, 0x105, 400)
    Sleep(300)

    label("loc_2704")


    ChrTalk(    #43
        0x101,
        "#1016F#6PYeah...me, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2725")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2852")

    ChrTalk(    #44
        0x104,
        (
            "#034FAh, I would have loved to sing the\x01",
            "battle between Zin and Walter!\x02\x03",

            "#030FAh, well.\x01",
            "There is always the next time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C7")
    TurnDirection(0x101, 0x104, 400)
    Sleep(300)

    label("loc_27C7")


    ChrTalk(    #45
        0x101,
        (
            "#1004F#6PNext...\x02\x03",

            "#1019FI thought you were going back to\x01",
            "being a PRINCE after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x104,
        "#031FHa! But are they mutually exclusive?\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_2852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297E")

    ChrTalk(    #47
        0x109,
        (
            "#1062FHmm. The passionate battle between\x01",
            "two men for one woman!\x02\x03",

            "#1061FMan, you can just feel the romance\x01",
            "comin' off the pages!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28FE")
    TurnDirection(0x101, 0x109, 400)
    Sleep(300)

    label("loc_28FE")


    ChrTalk(    #48
        0x101,
        (
            "#1016F#6PY'know, I don't think it's really a fight over\x01",
            "Kilika...(Partially 'cause I think she could\x01",
            "take them both...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FE")

    label("loc_297E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FE")

    ChrTalk(    #49
        0x110,
        (
            "#272F(He was a very competent fighter.)\x02\x03",

            "#276F(If that was a one-on-one match,\x01",
            "I might have been in danger.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FE")


    ChrTalk(    #50
        0x102,
        (
            "#1040F#4PEither way, we can proceed now.\x02\x03",

            "Let's use the terminal to unlock the gate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #51
        0x101,
        "#1006F#6PYeah, let's!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2234)
    OP_28(0x9F, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_11_1681 end

    def Function_12_2A86(): pass

    label("Function_12_2A86")

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

    # Function_12_2A86 end

    def Function_13_2B14(): pass

    label("Function_13_2B14")


    def lambda_2B1A():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B1A)
    Sleep(80)

    def lambda_2B3A():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B3A)
    Sleep(100)

    def lambda_2B5A():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2B5A)
    Sleep(150)
    OP_8E(0xF9, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
    Return()

    # Function_13_2B14 end

    def Function_14_2B89(): pass

    label("Function_14_2B89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B9E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_14_2B89")

    label("loc_2B9E")

    Return()

    # Function_14_2B89 end

    def Function_15_2B9F(): pass

    label("Function_15_2B9F")


    def lambda_2BA5():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2BA5)

    def lambda_2BC0():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2BC0)
    Sleep(500)

    def lambda_2BE0():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2BE0)

    def lambda_2BFB():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2BFB)
    Sleep(500)

    def lambda_2C1B():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C1B)

    def lambda_2C36():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2C36)
    Sleep(400)

    def lambda_2C56():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C56)

    def lambda_2C71():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2C71)
    Sleep(300)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x8, 0x1)

    def lambda_2C9B():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2C9B)

    def lambda_2CB6():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CB6)
    Sleep(200)

    def lambda_2CD6():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2CD6)

    def lambda_2CF1():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CF1)
    Sleep(100)

    def lambda_2D11():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D11)

    def lambda_2D2C():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D2C)
    Sleep(100)

    def lambda_2D4C():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D4C)

    def lambda_2D67():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D67)
    Return()

    # Function_15_2B9F end

    def Function_16_2D7D(): pass

    label("Function_16_2D7D")

    OP_8E(0xFE, 0xFFFFB6FE, 0x0, 0x3138, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_2D7D end

    def Function_17_2D99(): pass

    label("Function_17_2D99")

    OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0x3214, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_2D99 end

    def Function_18_2DB5(): pass

    label("Function_18_2DB5")

    OP_8E(0xFE, 0xFFFFB82A, 0x0, 0x2B5C, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_2DB5 end

    def Function_19_2DD1(): pass

    label("Function_19_2DD1")

    OP_8E(0xFE, 0xFFFFBE10, 0x0, 0x2BA2, 0x1770, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_2DD1 end

    def Function_20_2DED(): pass

    label("Function_20_2DED")

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

    def lambda_2E84():
        OP_6B(3960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E84)

    def lambda_2E94():
        OP_8E(0xFE, 0x4556, 0x0, 0xFFFFFE5C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E94)
    Sleep(80)

    def lambda_2EB4():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EB4)
    Sleep(100)

    def lambda_2ED4():
        OP_8E(0xFE, 0x4A6A, 0x0, 0xFFFFFD6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2ED4)
    Sleep(150)

    def lambda_2EF4():
        OP_8E(0xFE, 0x49C0, 0x0, 0x2D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2EF4)
    FadeToBright(1000, 0)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x8, 15)
    SetChrPos(0x8, -18090, 0, 240, 90)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #52
        0x8,
        "Man's Voice",
        (
            "FINALLY.\x01",
            "Was gettin' tired waitin' up here.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3042")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3001")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_303F")

    label("loc_3001")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3028")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_303F")

    label("loc_3028")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_303F")

    Jump("loc_30A7")

    label("loc_3042")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3069")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_30A7")

    label("loc_3069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3090")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_30A7")

    label("loc_3090")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_30A7")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30C9")

    ChrTalk(    #53
        0x110,
        "#270FHmm?\x02",
    )

    CloseMessageWindow()

    label("loc_30C9")

    OP_1D(0x6F)
    Sleep(500)

    def lambda_30D6():
        OP_6D(-18810, 0, 1110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30D6)

    def lambda_30EE():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30EE)

    def lambda_3106():
        OP_6B(3430, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3106)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #54
        0x101,
        "#1005F#1PSunglasses guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1042FThe Direwolf.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 17480, 0, -710, 270)
    SetChrPos(0x102, 17440, 0, 930, 270)
    SetChrPos(0x108, 16010, 0, 200, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A5")
    SetChrPos(0xF9, 18670, 0, 90, 270)
    Jump("loc_31B6")

    label("loc_31A5")

    SetChrPos(0xF8, 18670, 0, 90, 270)

    label("loc_31B6")


    def lambda_31BC():
        OP_8E(0xFE, 0xFFFFD8AA, 0x0, 0xD2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_31BC)

    def lambda_31D7():
        OP_6D(-13930, 0, 1180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31D7)

    def lambda_31EF():
        OP_67(0, 3910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31EF)

    def lambda_3207():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3207)

    def lambda_3217():
        OP_6E(311, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3217)
    Sleep(50)

    def lambda_322C():
        OP_8E(0xFE, 0xFFFFDE04, 0x0, 0xFFFFFB50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_322C)
    Sleep(100)

    def lambda_324C():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_324C)
    Sleep(40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3291")

    def lambda_3279():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFE66, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3279)
    Jump("loc_32AC")

    label("loc_3291")


    def lambda_3297():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFFE66, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3297)

    label("loc_32AC")

    WaitChrThread(0x102, 0x2)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DF")
    SetChrChipByIndex(0xF9, 8)
    Jump("loc_32E4")

    label("loc_32DF")

    SetChrChipByIndex(0xF8, 8)

    label("loc_32E4")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x108,
        "#572F#4PWalter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#251F#6PHeh. Nice of you to come.\x02\x03",

            "If YOU'RE here, I assume that means\x01",
            "you're ready, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x108,
        (
            "#074F#4PYes. It is time.\x02\x03",

            "#072FI will use the Living Fist of our master\x01",
            "to shatter your Murderer's Fist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#257F#6PHeh heh heh.\x02\x03",

            "You ended up just like the old\x01",
            "man said you would.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x108,
        (
            "#073F#4PAs...Master Ryuga said I would?\x02\x03",

            "#076FWhat do you mean, Walter?\x02\x03",

            "So your fight with Master DID\x01",
            "have something to do with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#253F#6PHah, I told you, didn't I?\x02\x03",

            "If you wanna know, beat me.\x02",
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

    def lambda_35A6():
        OP_6D(-31560, 5700, 0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35A6)

    def lambda_35BE():
        OP_67(0, 6700, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35BE)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    SetChrPos(0x108, -9000, 0, 210, 270)
    SetChrPos(0x101, -7300, 0, -770, 270)
    SetChrPos(0x102, -7300, 0, 1190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362E")
    SetChrPos(0xF9, -5040, 0, 240, 270)
    Jump("loc_363F")

    label("loc_362E")

    SetChrPos(0xF8, -5040, 0, 240, 270)

    label("loc_363F")

    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_43(0xA, 0x0, 0x0, 0x9)
    Sleep(100)

    def lambda_3669():
        OP_6D(-13900, 500, 410, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3669)

    def lambda_3681():
        OP_67(0, 3000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3681)

    def lambda_3699():
        OP_6E(288, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3699)

    def lambda_36A9():
        OP_6B(3670, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_36A9)
    Sleep(100)
    OP_43(0xB, 0x0, 0x0, 0xA)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xB, 0x0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)

    def lambda_36E2():
        OP_6C(270000, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36E2)
    OP_71(0x0, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #62
        0x8,
        (
            "#257FYou swing some coward's fist\x01",
            "at me, and I'll end you right here.\x02\x03",

            "#253FC'mon! Time for a good,\x01",
            "old-fashioned death match!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3781():
        OP_6D(-13930, 500, 410, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3781)

    def lambda_3799():
        OP_67(0, 2920, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3799)

    def lambda_37B1():
        OP_6B(3000, 250)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37B1)
    SetChrChipByIndex(0x108, 20)
    SetChrFlags(0x108, 0x1000)

    def lambda_37CB():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_37CB)
    Sleep(30)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 2)

    def lambda_37FA():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x15E, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_37FA)
    OP_44(0xA, 0x3)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1000)

    def lambda_3830():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3830)

    def lambda_3840():
        OP_91(0xFE, 0x1388, 0x0, 0x7D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3840)

    def lambda_385B():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_385B)

    def lambda_3876():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3876)
    Sleep(30)
    OP_44(0xB, 0x3)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x1000)

    def lambda_38AE():
        OP_99(0xFE, 0x0, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_38AE)

    def lambda_38BE():
        OP_91(0xFE, 0x1388, 0x0, 0xFFFFF830, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_38BE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3903")
    SetChrChipByIndex(0xF9, 8)

    def lambda_38EB():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_38EB)
    Jump("loc_3923")

    label("loc_3903")

    SetChrChipByIndex(0xF8, 8)

    def lambda_390E():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_390E)

    label("loc_3923")

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

    # Function_20_2DED end

    def Function_21_3956(): pass

    label("Function_21_3956")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A70")
    SetChrPos(0xF9, -9200, 0, 0, 270)
    Jump("loc_3A81")

    label("loc_3A70")

    SetChrPos(0xF8, -9200, 0, 0, 270)

    label("loc_3A81")

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

    def lambda_3AFB():
        OP_6D(-19390, 0, 1500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AFB)
    OP_67(0, 5210, -10000, 3000)
    OP_0D()
    Fade(500)
    StopSound(0x11170, 0x29810, 0x0)
    OP_6B(4270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #63
        0x8,
        (
            "#259F#5PSon of a...\x02\x03",

            "The hell did you...learn that kinda...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        (
            "#074FWalter...as always, you are a genius.\x02\x03",

            "But your talents mean you've never\x01",
            "practiced as you should.\x02\x03",

            "#072FAnd the way of the fist is built on\x01",
            "training. Always training, so that it\x01",
            "comes naturally as breathing.\x02\x03",

            "That's why even I, your lesser, can\x01",
            "strike you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#255F#5P...\x02\x03",

            "#257FHeh. My lesser, huh?\x02\x03",

            "#253FThe old man didn't think so,\x01",
            "you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x108,
        "#073F...What?\x02",
    )

    CloseMessageWindow()
    OP_1D(0x53)
    Sleep(500)

    def lambda_3D0C():
        OP_6B(3600, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D0C)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        (
            "#253FThe old man told me this.\x02\x03",

            "Puttin' aside all the bullshit about the\x01",
            "ideal of a 'living fist' or a 'murderer's fist'\x01",
            "or whatever...\x02\x03",

            "In terms of pure talent and quality...\x01",
            "you're better than me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #68
        0x108,
        "#076FYou... You can't be serious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#253F#5PAnd the old man said he was going\x01",
            "to have the most talented one inherit\x01",
            "the Taito style.\x02\x03",

            "Now, you are the densest lump o'\x01",
            "meat I've ever known, Zin, but even\x01",
            "you know what that'd mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x108,
        (
            "#075FBut that... How...?\x02\x03",

            "#072FI'm better than you?\x01",
            "That's absurd! It's a blatant lie!\x02\x03",

            "And Master would never have done that\x01",
            "and just ignored Kilika's feelings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#250FHeh heh... You're naive as ever.\x02\x03",

            "That's just it. To be with our teacher's\x01",
            "daughter, without inheriting the school?\x02\x03",

            "You think I'd accept that?\x01",
            "Hell... I wonder if she'd accept that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        "#572F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#251FSo, you see, I demanded a match\x01",
            "with you to determine the successor.\x02\x03",

            "And then the old man laid another\x01",
            "one on me.\x02\x03",

            "#257F'Zin unconsciously submits to you\x01",
            "in all things.'\x02\x03",

            "'Both in martial arts and affairs of the\x01",
            "heart.'\x02\x03",

            "#255F'As long as you both are as you are\x01",
            "now...you would never truly fight him.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x108,
        "#073FBut, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#253F#5PHeh... I was still a young hothead,\x01",
            "so I really couldn't accept that.\x02\x03",

            "So once I kept insisting, he said\x01",
            "HE'D fight a deathmatch with me\x01",
            "in your place.\x02\x03",

            "#257FAnd then...I won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x108,
        "#072F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#253F#5PSo. That's why I killed the old man.\x02\x03",

            "You wanted to know, so I answered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x108,
        (
            "#074F...\x02\x03",

            "I think I finally understand.\x02\x03",

            "I could never understand why Master\x01",
            "asked to fight that match with you...\x02\x03",

            "#572FBut now the pieces have finally fallen\x01",
            "into place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#255F#5PHave they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x108,
        (
            "#072FThere's something you don't\x01",
            "understand, Walter.\x02\x03",

            "I only learned about this from Kilika\x01",
            "after the match. But...\x02\x03",

            "#074FMaster Ryuga had just learned he\x01",
            "had cancer when you challenged him.\x02\x03",

            "Terminal cancer, that is.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x8,
        "#258F#5PWait a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x108,
        (
            "#072FTHAT is why he challenged you, Walter.\x02\x03",

            "I'm sure he also wanted to admonish\x01",
            "your abuse of the Taito style...\x02\x03",

            "And he wanted to show me the pinnacle\x01",
            "of the art, and inspire me to step out of\x01",
            "your shadow.\x02\x03",

            "#572FBut, more than anything, what Master\x01",
            "wanted...\x02\x03",

            "#074F...was to end his life in battle against\x01",
            "his greatest student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#254F#5P...\x02\x03",

            "#252FHeh. Heh, heh. The hell is this...?\x02\x03",

            "Ridiculous. No way.\x02\x03",

            "So, what? He just used me as a\x01",
            "tool for suicide?\x02\x03",

            "If that's true, then all I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x108,
        (
            "#074FOn some level, it was deeply selfish,\x01",
            "it's true.\x02\x03",

            "#072FBut when you think about it, trying to\x01",
            "perfect yourself and your power is a\x01",
            "selfish act, no matter what else you do.\x02\x03",

            "You could say a dedication to selfishness\x01",
            "is our duty as martial artists.\x02\x03",

            "#572FI think Master...chose to put all his\x01",
            "selfishness on display.\x02\x03",

            "And, in doing so, revealed to both of\x01",
            "us the light and darkness of the fist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "#254F#5PFeh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x108, 21)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0x108,
        "#072FWalter. Take your stance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        "#255F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x108,
        (
            "#072FI shall put everything I have learned, from you\x01",
            "and from Master...everything I've practiced\x01",
            "as a bracer...all of Taito into this fist.\x02\x03",

            "And I shall use it to bring light to the foolish\x01",
            "elder student before me, who has become\x01",
            "a devil and fallen into darkness.\x02\x03",

            "#074FIt is my final duty as the dojo's junior student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#255F#5P...\x02\x03",

            "#257FHeh. Look at you, bein' all like the\x01",
            "old man...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #90
        0x8,
        (
            "#253FAll right.\x02\x03",

            "I'll put everything I've perfected in\x01",
            "the society into my fist...to bury Taito\x01",
            "forever.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-19320, 0, 0, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -8300, 0, -600, 270)
    SetChrPos(0x102, -8400, 0, 800, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B37")
    SetChrPos(0xF9, -7200, 0, 0, 270)
    Jump("loc_4B48")

    label("loc_4B37")

    SetChrPos(0xF8, -7200, 0, 0, 270)

    label("loc_4B48")

    OP_71(0x0, 0x4)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #91
        0x108,
        "#072F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#255F#1P...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearMapFlags(0x10)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 12)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 16)
    OP_0D()

    def lambda_4C09():
        OP_99(0xFE, 0x0, 0x7, 0x708)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4C09)

    def lambda_4C19():
        OP_99(0xFE, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C19)
    WaitChrThread(0x8, 0x1)
    Sleep(700)

    def lambda_4C33():

        label("loc_4C33")

        OP_7C(0x64, 0x0, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_4C33")

    QueueWorkItem2(0x101, 3, lambda_4C33)
    OP_22(0x85, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #93
        0x108,
        "#077F#1K#4PHAAAAAAAAAAA!\x02",
    )


    ChrTalk(    #94
        0x8,
        "#259F#1K#1PKOOOOOOOOOOH!\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(1000)
    OP_6D(-13000, 0, 0, 1500)
    Sleep(500)

    ChrTalk(    #95
        0x101,
        "#1020F#5P(This is nuts!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        "#1043F#2P(One of them HAS to break...)\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_4D35():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D35)

    ChrTalk(    #97 op#A op#5
        0x108,
        "#076F#4P#30AHOOOOOOOOOOOOO!\x05\x02",
    )


    ChrTalk(    #98 op#A op#5
        0x8,
        "#258F#1P#30ARAAAAAAAAAAAAGH!\x05\x02",
    )

    Sleep(5000)
    OP_56(0x0)
    WaitChrThread(0x101, 0x2)

    def lambda_4D94():
        OP_6B(3000, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D94)
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

    def lambda_4DD5():
        OP_8E(0xFE, 0xFFFFB956, 0x0, 0xEA6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4DD5)

    def lambda_4DF0():
        OP_8E(0xFE, 0xFFFFB956, 0x0, 0xFFFFF33A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4DF0)
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

    ChrTalk(    #99
        0x8,
        "#254F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x108,
        (
            "#074F#5P...\x02\x03",

            "#572F...Gh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 11)
    OP_99(0x108, 0x0, 0x1, 0x4B0)

    def lambda_4F41():
        OP_6D(-19390, 0, -500, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F41)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x108, 0x1, 0x3, 0x4B0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #101
        0x102,
        "#1044F#1PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1020F#1PZin!\x02",
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

    ChrTalk(    #103
        0x8,
        "#253F#4P#40WHeh...heh...heh... You fool...\x02",
    )

    CloseMessageWindow()

    def lambda_5012():
        OP_6D(-19390, 0, 3500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5012)
    OP_99(0x8, 0x0, 0x4, 0x3E8)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(1000)
    OP_99(0x8, 0x4, 0x6, 0x320)
    Sleep(200)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #104
        0x8,
        (
            "#253F#4P#40WYou were holdin' back like THAT...?\x02\x03",

            "#257F#40W...Shit.\x01",
            "Ryuga was right...\x02\x03",

            "#250F#60WAaah...\x02\x03",

            "#80WWhy does this stuff...\x01",
            "have to taste so...good...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 24)
    OP_99(0x8, 0x18, 0x1E, 0x5DC)
    Sleep(200)

    def lambda_5113():
        OP_6D(-19390, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5113)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5215")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D4")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5212")

    label("loc_51D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51FB")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5212")

    label("loc_51FB")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5212")

    Jump("loc_527A")

    label("loc_5215")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_523C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_527A")

    label("loc_523C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5263")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_527A")

    label("loc_5263")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_527A")

    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x101,
        "#1025F#5PHe did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        "#1040F#2PZin won. I knew he could.\x02",
    )

    CloseMessageWindow()

    def lambda_52E2():
        OP_6D(-17900, 0, -2700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_52E2)

    def lambda_52FA():
        OP_67(0, 5260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_52FA)

    def lambda_5312():
        OP_6B(3580, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5312)
    OP_43(0x101, 0x1, 0x0, 0x17)
    Sleep(200)
    OP_43(0x102, 0x1, 0x0, 0x18)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534B")
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Jump("loc_5352")

    label("loc_534B")

    OP_43(0xF8, 0x1, 0x0, 0x1A)

    label("loc_5352")

    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539B")

    ChrTalk(    #107
        0x106,
        "#051FHah, nice!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_539B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53C6")

    ChrTalk(    #108
        0x103,
        "#021FZin, well done!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_53C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53F1")

    ChrTalk(    #109
        0x110,
        "#275FVery well done!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_53F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5425")

    ChrTalk(    #110
        0x104,
        "#031FAh! A masterful victory!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5425")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_545F")

    ChrTalk(    #111
        0x109,
        "#1061FHoooo, man, that was amazing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_545F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5499")

    ChrTalk(    #112
        0x10F,
        "#171FAn amazing victory, Mr. Vathek\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54CE")

    ChrTalk(    #113
        0x105,
        "#1168FThat was wonderful, Zin!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_54CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5502")

    ChrTalk(    #114
        0x107,
        "#067FWooow! That was so cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5502")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5544")

    ChrTalk(    #115
        0x10B,
        "#210FWell, that was definitely pretty awesome!\x02",
    )

    CloseMessageWindow()

    label("loc_5544")


    ChrTalk(    #116
        0x101,
        (
            "#1001F#2PYeah! That was great!\x02\x03",

            "#1018FI, uh, didn't think you could really\x01",
            "beat that guy in a straight-up fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x108,
        "#074F#6PNo.\x02",
    )

    CloseMessageWindow()

    def lambda_55D1():

        label("loc_55D1")

        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0x7D0)
        OP_48()
        Jump("loc_55D1")

    QueueWorkItem2(0x108, 3, lambda_55D1)
    Sleep(300)
    OP_99(0x108, 0x3, 0x0, 0x320)
    OP_44(0x108, 0x3)
    Fade(500)
    SetChrChipByIndex(0x108, 65535)
    SetChrSubChip(0x108, 0)
    OP_0D()

    def lambda_5610():
        OP_8C(0x102, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5610)
    Sleep(200)
    OP_8C(0x108, 90, 300)
    Sleep(500)

    ChrTalk(    #118
        0x108,
        (
            "#074F#6PThe reason I won is solely because\x01",
            "I bear the Taito style.\x02\x03",

            "#572FIf he'd fought me as a proper user of Taito...\x01",
            "If he'd just applied what he learned...\x02\x03",

            "I'd be the one sprawled out on the floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1016F#2PAww, I don't think that's true!\x01",
            "Give yourself SOME credit!\x02\x03",

            "#1015FOh, more importantly, Zin...\x01",
            "Are you okay? You're not hurt,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        (
            "#1044FWe can get you some help,\x01",
            "if you need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x108,
        (
            "#074F#6PNo... I'm fine.\x02\x03",

            "#070FWalter will likely be out for a while,\x01",
            "so we can leave him here, I think.\x02\x03",

            "We need to keep heading up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1006F#2PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#1040FLet's deal with the terminal, then.\x02",
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

    # Function_21_3956 end

    def Function_22_58F8(): pass

    label("Function_22_58F8")


    def lambda_58FE():
        OP_8E(0xFE, 0x44AC, 0x0, 0x352, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58FE)
    Sleep(40)

    def lambda_591E():
        OP_8E(0xFE, 0x448E, 0x0, 0xFFFFFF24, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_591E)
    Sleep(100)

    def lambda_593E():
        OP_8E(0xFE, 0x4916, 0x0, 0x4F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593E)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_597C")
    OP_8E(0xF9, 0x48C6, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)
    Jump("loc_5990")

    label("loc_597C")

    OP_8E(0xF8, 0x48C6, 0x0, 0xFFFFFCF4, 0xBB8, 0x0)

    label("loc_5990")

    Return()

    # Function_22_58F8 end

    def Function_23_5991(): pass

    label("Function_23_5991")

    OP_8E(0xFE, 0xFFFFC00E, 0x0, 0xFFFFEF8E, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_5991 end

    def Function_24_59AD(): pass

    label("Function_24_59AD")

    OP_8E(0xFE, 0xFFFFBF6E, 0x0, 0xFFFFF452, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_59AD end

    def Function_25_59C9(): pass

    label("Function_25_59C9")

    OP_8E(0xFE, 0xFFFFC428, 0x0, 0xFFFFF150, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_59C9 end

    def Function_26_59E5(): pass

    label("Function_26_59E5")

    OP_8E(0xFE, 0xFFFFC428, 0x0, 0xFFFFF150, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_26_59E5 end

    def Function_27_5A01(): pass

    label("Function_27_5A01")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #124
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
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

    # Function_27_5A01 end

    def Function_28_5A77(): pass

    label("Function_28_5A77")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8E")
    Call(0, 30)
    Call(0, 31)

    label("loc_5A8E")

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
    SetChrName("Voice")

    AnonymousTalk(    #125
        "\x07\x05Barrier to upper levels and transport gate now unlocked.\x02",
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

    # Function_28_5A77 end

    def Function_29_5B92(): pass

    label("Function_29_5B92")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA9")
    Call(0, 30)
    Call(0, 31)

    label("loc_5BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BBE")
    Call(0, 6)
    Jump("loc_5BC2")

    label("loc_5BBE")

    Call(0, 20)

    label("loc_5BC2")

    Return()

    # Function_29_5B92 end

    def Function_30_5BC3(): pass

    label("Function_30_5BC3")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C3C"),
        (1, "loc_5C42"),
        (SWITCH_DEFAULT, "loc_5C48"),
    )


    label("loc_5C3C")

    OP_A2(0x1200)
    Jump("loc_5C48")

    label("loc_5C42")

    OP_A2(0x1201)
    Jump("loc_5C48")

    label("loc_5C48")

    Return()

    # Function_30_5BC3 end

    def Function_31_5C49(): pass

    label("Function_31_5C49")

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

    # Function_31_5C49 end

    def Function_32_5CDC(): pass

    label("Function_32_5CDC")

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

    # Function_32_5CDC end

    SaveToFile()

Try(main)
