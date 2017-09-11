from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3170   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3170.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3170   ._SN',
            'ED6_DT01/T3170_1 ._SN',
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
        'Dodge',                                # 9
        'Ben',                                  # 10
        'Ursus',                                # 11
        'Randall',                              # 12
        'Cosimo',                               # 13
        'Igor',                                 # 14
        'Rehmann',                              # 15
        'Constance',                            # 16
        'Ray',                                  # 17
        'Terry',                                # 18
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
        'ED6_DT07/CH01143 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01000 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01250 ._CH',             # 05
        'ED6_DT07/CH01450 ._CH',             # 06
        'ED6_DT07/CH01230 ._CH',             # 07
        'ED6_DT07/CH01220 ._CH',             # 08
        'ED6_DT07/CH01663 ._CH',             # 09
        'ED6_DT07/CH01223 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01143P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01000P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01250P._CP',             # 05
        'ED6_DT07/CH01450P._CP',             # 06
        'ED6_DT07/CH01230P._CP',             # 07
        'ED6_DT07/CH01220P._CP',             # 08
        'ED6_DT07/CH01663P._CP',             # 09
        'ED6_DT07/CH01223P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_63E",          # 01, 1
        "Function_2_6B2",          # 02, 2
        "Function_3_6C8",          # 03, 3
        "Function_4_6EC",          # 04, 4
        "Function_5_710",          # 05, 5
        "Function_6_734",          # 06, 6
        "Function_7_963",          # 07, 7
        "Function_8_DE0",          # 08, 8
        "Function_9_1099",         # 09, 9
        "Function_10_13D4",        # 0A, 10
        "Function_11_154A",        # 0B, 11
        "Function_12_154B",        # 0C, 12
        "Function_13_1550",        # 0D, 13
        "Function_14_28C2",        # 0E, 14
        "Function_15_33E8",        # 0F, 15
        "Function_16_3C3A",        # 10, 16
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    Jump("loc_63D")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_34A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1800, 4000, 7110, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    OP_43(0x9, 0x0, 0x0, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -260, 4000, 7710, 192)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -540, -1000, 4640, 270)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 10)
    SetChrPos(0x10, -2630, 4200, 7900, 182)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -3800, 4200, 6600, 90)
    SetChrFlags(0x11, 0x10)
    Jump("loc_63D")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1200, -1000, 5200, 97)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)
    Jump("loc_63D")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4B8")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_50B")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1200, -1000, 5200, 97)
    OP_43(0xB, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 640, -1000, 6620, 9)
    Jump("loc_63D")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_557")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3450, -1000, 8500, 185)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5A3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)
    Jump("loc_63D")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_63D")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)

    label("loc_63D")

    Return()

    # Function_0_266 end

    def Function_1_63E(): pass

    label("Function_1_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_648")
    Jump("loc_6B1")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_652")
    Jump("loc_6B1")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_6B1")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_66A")
    OP_64(0x0, 0x1)
    Jump("loc_6B1")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_6B1")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_67E")
    Jump("loc_6B1")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_68C")
    OP_64(0x0, 0x1)
    Jump("loc_6B1")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_696")
    Jump("loc_6B1")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Jump("loc_6B1")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6AA")
    Jump("loc_6B1")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6B1")

    label("loc_6B1")

    Return()

    # Function_1_63E end

    def Function_2_6B2(): pass

    label("Function_2_6B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6B2")

    label("loc_6C7")

    Return()

    # Function_2_6B2 end

    def Function_3_6C8(): pass

    label("Function_3_6C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB")
    OP_8D(0xFE, -1880, 8780, 440, 8570, 3000)
    Jump("Function_3_6C8")

    label("loc_6EB")

    Return()

    # Function_3_6C8 end

    def Function_4_6EC(): pass

    label("Function_4_6EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70F")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 3000)
    Jump("Function_4_6EC")

    label("loc_70F")

    Return()

    # Function_4_6EC end

    def Function_5_710(): pass

    label("Function_5_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_8D(0xFE, -1460, 6310, 0, 9500, 3000)
    Jump("Function_5_710")

    label("loc_733")

    Return()

    # Function_5_710 end

    def Function_6_734(): pass

    label("Function_6_734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C4")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BF"),
        (1, "loc_85D"),
        (SWITCH_DEFAULT, "loc_8BD"),
    )


    label("loc_7BF")


    ChrTalk(    #0
        0xFE,
        (
            "I wouldn't call a scheme pulled out\x01",
            "of your rear end 'forward thinking.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Branding that disgusting tomato isn't\x01",
            "going to make it sell any better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BD")

    label("loc_85D")


    ChrTalk(    #2
        0xFE,
        (
            "I'm sorry, but I'm finished with\x01",
            "my work for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Come back and ask me tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BD")

    label("loc_8BD")

    TalkEnd(0xFE)
    Return()

    label("loc_8C4")


    ChrTalk(    #4
        0xFE,
        (
            "I wouldn't call a scheme pulled out\x01",
            "of your rear end 'forward thinking.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Branding that disgusting tomato isn't\x01",
            "going to make it sell any better.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_734 end

    def Function_7_963(): pass

    label("Function_7_963")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_A05")

    ChrTalk(    #6
        0xFE,
        (
            "Terry, you're just not forward-\x01",
            "thinking enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "You've got to be ready to make\x01",
            "lemonade with the box of\x01",
            "chocolates life hands you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_A05")

    OP_A2(0x8)

    ChrTalk(    #8
        0xFE,
        (
            "Terry, you're just not forward-\x01",
            "thinking enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Take that bitter tomato. All we\x01",
            "need to do is brand it properly,\x01",
            "and it'll sell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "We could call it something inspired\x01",
            "like...'The Bitter Tomato'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Or maybe go by a more...scientific sounding\x01",
            "moniker. Hmm...'The Acerbic Tomato'?\x01",
            "Certainly SOUNDS officious enough...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B54")

    Jump("loc_DDC")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_C52")

    ChrTalk(    #12
        0xFE,
        (
            "When we're working we usually\x01",
            "end up eating traditional foods\x01",
            "found in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Terry is having some serious\x01",
            "problems keeping up with us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Being shut up in your lab all\x01",
            "day isn't the best way to find\x01",
            "some inspiration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC")

    label("loc_C52")

    OP_A2(0x8)

    ChrTalk(    #15
        0xFE,
        (
            "When we're working we usually\x01",
            "end up eating traditional foods\x01",
            "found in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It doesn't have much going for\x01",
            "it in terms of subtlety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "But if you need something to jolt\x01",
            "your head back into the game,\x01",
            "Zeiss cooking is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I'd really like to see some\x01",
            "measures taken to allow\x01",
            "us to choose our meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Who knows? Inspiration can\x01",
            "sometimes come from the\x01",
            "strangest places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC")

    TalkEnd(0xFE)
    Return()

    # Function_7_963 end

    def Function_8_DE0(): pass

    label("Function_8_DE0")

    SetChrFlags(0xF, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_E58")

    ChrTalk(    #20
        0xFE,
        (
            "Today was an especially\x01",
            "exhausting day for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I need to blow off all\x01",
            "this stress...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1095")

    label("loc_E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EC7")

    ChrTalk(    #22
        0xFE,
        (
            "Today was an especially\x01",
            "exhausting day for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I need to blow off all\x01",
            "this stress...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_1095")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_F6C")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #24
        0xFE,
        "Did you bring that book?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Looks like you did...but I'm\x01",
            "off right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Can we not talk about work?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_8C(0xFE, 270, 400)
    Jump("loc_1095")

    label("loc_F6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1033")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #27
        0xFE,
        (
            "Did you want to ask me\x01",
            "something about work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Looks like you brought the book...\x01",
            "but I'm off right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Can we not talk about work?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_8C(0xFE, 270, 400)
    Jump("loc_1095")

    label("loc_1033")


    ChrTalk(    #30
        0xFE,
        (
            "Today was an especially\x01",
            "exhausting day for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I need to blow off all\x01",
            "this stress...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_1095")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE0 end

    def Function_9_1099(): pass

    label("Function_9_1099")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1127")

    ChrTalk(    #32
        0xFE,
        (
            "Here I am, aid to the heroic rescue\x01",
            "of Professor Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "...and I'm not allowed to brag\x01",
            "to anybody about it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_1127")

    OP_A2(0x6)

    ChrTalk(    #34
        0xFE,
        (
            "Yeah, I heard you did a number\x01",
            "on Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I feel proud enough being on\x01",
            "the team and helping from\x01",
            "the sidelines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "But I was a little nervous when\x01",
            "all those soldiers surrounded\x01",
            "the container.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "We can look back and laugh\x01",
            "about it now. But at the time,\x01",
            "we all nearly peed ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    Jump("loc_13D0")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_12FD")

    ChrTalk(    #38
        0xFE,
        (
            "Tomorrow I've got to take a\x01",
            "factory ship out to Leiston\x01",
            "Fortress again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Recently the army has been\x01",
            "placing all kinds of orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_12FD")

    OP_A2(0x6)

    ChrTalk(    #40
        0xFE,
        (
            "Tomorrow I've got to take a\x01",
            "factory ship out to Leiston\x01",
            "Fortress again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Everybody's busy getting all the\x01",
            "prep work taken care of...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Times like this make me glad\x01",
            "I'm a pilot, and not a laborer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1099 end

    def Function_10_13D4(): pass

    label("Function_10_13D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_147A")

    ChrTalk(    #43
        0xFE,
        (
            "I came all this way just to see\x01",
            "Randall and wouldn't you know,\x01",
            "he's already gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Oh well. May as well order up\x01",
            "an old favorite or two.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_147A")

    OP_A2(0x4)

    ChrTalk(    #45
        0xFE,
        "Hmph. Just my luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I came all this way just to see\x01",
            "Randall and wouldn't you know,\x01",
            "he's already gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "He's the kind of guy you're\x01",
            "always just missin'. Been\x01",
            "like that since he was young.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    TalkEnd(0xFE)
    Return()

    # Function_10_13D4 end

    def Function_11_154A(): pass

    label("Function_11_154A")

    Return()

    # Function_11_154A end

    def Function_12_154B(): pass

    label("Function_12_154B")

    Call(0, 13)
    Return()

    # Function_12_154B end

    def Function_13_1550(): pass

    label("Function_13_1550")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1607")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Shop\x01",                  # 1
            "Show ingredients\x01",      # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DB")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_15DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F3")
    Call(1, 2)
    TalkEnd(0x9)
    Return()

    label("loc_15F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1604")
    TalkEnd(0x9)
    Return()

    label("loc_1604")

    Jump("loc_1675")

    label("loc_1607")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1664")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1664")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1675")
    TalkEnd(0x9)
    Return()

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_16CD")

    ChrTalk(    #48
        0x9,
        "Thanks for today, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "Keep an eye out for my\x01",
            "latest creation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_16CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F2")

    ChrTalk(    #50
        0x9,
        (
            "Lately I've been hearing about\x01",
            "this strange tomato they grew\x01",
            "in the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "I got a sample to see if I\x01",
            "could use it somehow...and\x01",
            "it is INCREDIBLE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "I've already placed a big\x01",
            "advance order for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "I plan to feature them on the\x01",
            "menu, so watch for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_17F2")

    OP_A2(0x1)

    ChrTalk(    #54
        0x9,
        (
            "Hey, you guys. I really want to\x01",
            "thank you for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "I was just on my way to the\x01",
            "factory to place an advance\x01",
            "order on those tomatoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "I should have them on the menu\x01",
            "in no time. Just wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_28BE")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1998")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #57
        0x9,
        "Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        "I just finished the lunch rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "How'd you like an EXTRA bitter\x01",
            "Tomato Sandwich?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#000FEr, pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1995")

    label("loc_1950")


    ChrTalk(    #61
        0x9,
        "Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        "I just finished the lunch rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        "Take a load off.\x02",
    )

    CloseMessageWindow()

    label("loc_1995")

    Jump("loc_28BE")

    label("loc_1998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1A3C")

    ChrTalk(    #64
        0x9,
        (
            "I've been working on some new\x01",
            "dishes lately that have really\x01",
            "been keeping me busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "I suppose I need to pace myself\x01",
            "so I don't fall over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AA4")

    ChrTalk(    #66
        0x9,
        "I've been really busy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "I suppose I need to pace myself\x01",
            "so I don't fall over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BA2")
    OP_A2(0xB)

    ChrTalk(    #68
        0x9,
        "I've been so busy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "In addition to my regular work\x01",
            "I've also been tinkering with\x01",
            "some new dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "If I keep this up I'm sure to\x01",
            "burn out sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "We working-class Joes need to\x01",
            "watch out for each other, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1BA2")

    OP_A2(0x1)

    ChrTalk(    #72
        0x9,
        "I've been real busy lately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "If I keep this up I'm sure to\x01",
            "burn out sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "We working-class Joes need to\x01",
            "watch out for each other, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_28BE")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1D70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D00")

    ChrTalk(    #75
        0x9,
        "Damn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "Ursus has gone home and Randall's\x01",
            "not around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "Guess I better get working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "I've got to finish those new\x01",
            "tomato dishes, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D6D")

    label("loc_1D00")


    ChrTalk(    #80
        0x9,
        "Damn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "Ursus has gone home and Randall's\x01",
            "not around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        "Guess I better get working.\x02",
    )

    CloseMessageWindow()

    label("loc_1D6D")

    Jump("loc_28BE")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E10")

    ChrTalk(    #84
        0x9,
        (
            "Sounds like there was a heck\x01",
            "of a fuss over at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "I bet some guys snuck in trying\x01",
            "to steal one of the new top-secret\x01",
            "experiments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_1E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1E6B")

    ChrTalk(    #86
        0x9,
        "Okay, Randall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "First I need you to have a\x01",
            "taste of this tomato.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2015")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1EA8")

    ChrTalk(    #88
        0x9,
        (
            "So, Randall. What are we talking\x01",
            "about today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2015")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F65")
    OP_A2(0xB)

    ChrTalk(    #89
        0x9,
        (
            "He's really been putting in some\x01",
            "hard work while Ursus has been\x01",
            "out of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "Today I think I'll leave the store\x01",
            "to him while I come up with\x01",
            "some new entrees.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2015")

    label("loc_1F65")

    OP_A2(0x1)

    ChrTalk(    #91
        0x9,
        (
            "He's really been putting in some\x01",
            "hard work while Ursus has been\x01",
            "out of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "Today I think I'll leave the store\x01",
            "to him while I come up with\x01",
            "some new entrees.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2015")

    Jump("loc_28BE")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2043")

    ChrTalk(    #93
        0x9,
        "Randall! Saute's up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2043")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2107")
    OP_A2(0x1)

    ChrTalk(    #94
        0x9,
        (
            "Right now Ursus isn't here, \x01",
            "so I've got to stir pots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "...but honestly, cooking can\x01",
            "be pretty interesting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "I've been coming up with so\x01",
            "many ideas for that tomato.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BD")

    label("loc_2107")

    OP_A2(0x1)

    ChrTalk(    #97
        0x9,
        (
            "Right now Ursus isn't here, \x01",
            "so I've got to stir pots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "...but honestly, cooking can\x01",
            "be pretty interesting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "I've been coming up with a lot\x01",
            "of ideas for new foods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BD")

    Jump("loc_28BE")

    label("loc_21C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(    #100
        0x9,
        (
            "But I really need something\x01",
            "that'll grab customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "I've pretty much exhausted all\x01",
            "the traditional stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "I need to add some new things\x01",
            "to the menu soon or else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2303")

    label("loc_2284")

    OP_A2(0x1)

    ChrTalk(    #103
        0x9,
        (
            "Everybody gets tired of the\x01",
            "same thing every day, be it\x01",
            "crackers or caviar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "Maybe he's just a selfish\x01",
            "old geezer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2303")

    Jump("loc_28BE")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2479")

    ChrTalk(    #105
        0x9,
        (
            "Of course it'll be a big problem if\x01",
            "orbments stopped again like they\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "Kids today can't even imagine a\x01",
            "world without orbments in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "Lights, heaters, vacuums, laundry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "Pretty much everything in our\x01",
            "daily life depends on having\x01",
            "the orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "Thinking about it that way really\x01",
            "makes you admire Professor\x01",
            "Russell even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_2479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_27E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_258A")

    ChrTalk(    #110
        0x9,
        (
            "People tied up in research have\x01",
            "always been seen as having...\x01",
            "health issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "That's how provincial Zeiss food\x01",
            "came about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "Easy to cook, easy to eat,\x01",
            "and nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "We Zeiss cooks all make our\x01",
            "recipes around those three\x01",
            "basic criteria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E0")

    label("loc_258A")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_END)), "loc_2664")

    ChrTalk(    #114
        0x9,
        (
            "Zeiss cooking is full of recipes\x01",
            "suited for engineers without\x01",
            "time to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "Easy to cook, easy to eat,\x01",
            "and nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "We Zeiss cooks all make our\x01",
            "recipes around those three\x01",
            "basic criteria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E0")

    label("loc_2664")

    OP_A2(0x576)

    ChrTalk(    #117
        0x9,
        (
            "Well, isn't this a treat!\x01",
            "How are you, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "And how's Professor Russell?\x01",
            "Same as ever, I trust?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x107,
        (
            "#060FYes, sir, he's doing well!\x02\x03",

            "He's been spending all of his\x01",
            "time lately working on new\x01",
            "experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "So in other words, ruining his\x01",
            "health like he always is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "Shouldn't he start acting\x01",
            "his age?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x9,
        (
            "You should try to get him\x01",
            "outside a little more often.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E0")

    Jump("loc_28BE")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2861")

    ChrTalk(    #123
        0x9,
        (
            "We serve traditional Zeiss\x01",
            "foods here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "'Simple and Efficient,' that's the\x01",
            "motto for Zeiss cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BE")

    label("loc_2861")

    OP_A2(0x1)

    ChrTalk(    #125
        0x9,
        (
            "Hello!  Haven't seen you all\x01",
            "before... Passing through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        "Well, come in and rest!\x02",
    )

    CloseMessageWindow()

    label("loc_28BE")

    TalkEnd(0x9)
    Return()

    # Function_13_1550 end

    def Function_14_28C2(): pass

    label("Function_14_28C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_29CA")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_295A")

    ChrTalk(    #127
        0xFE,
        (
            "It looks like Louise is going to be\x01",
            "busy with work for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I hope the new stuff Ben comes\x01",
            "up with tastes good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C7")

    label("loc_295A")

    OP_A2(0x2)

    ChrTalk(    #129
        0xFE,
        (
            "Lately Ben's been trying to think\x01",
            "of some new dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I'm a little...torn...about\x01",
            "the prospect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C7")

    Jump("loc_33E4")

    label("loc_29CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2A77")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2A13")

    ChrTalk(    #131
        0xFE,
        (
            "I sure hope Louise's work goes\x01",
            "smoothly for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_2A13")

    OP_A2(0x2)

    ChrTalk(    #132
        0xFE,
        (
            "Whew.\x01",
            "Finally, lunch hour is finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Things should be quiet now\x01",
            "until dinnertime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A74")

    Jump("loc_33E4")

    label("loc_2A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C07")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2B35")

    ChrTalk(    #134
        0xFE,
        (
            "Being dedicated to your job\x01",
            "is good and all, but everyone\x01",
            "needs a break sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "All work and no play...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "...makes me worry about turning\x01",
            "into Ben one day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C04")

    label("loc_2B35")

    OP_A2(0x2)

    ChrTalk(    #137
        0xFE,
        (
            "Yesterday I made this new soup\x01",
            "I just learned about and had\x01",
            "Louise eat some...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "She's been so busy lately she\x01",
            "hasn't had time to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "At least her sister, Yuriel, seemed\x01",
            "to enjoy it though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C04")

    Jump("loc_33E4")

    label("loc_2C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D17")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2CBB")

    ChrTalk(    #140
        0xFE,
        (
            "Louise has been all wrapped up\x01",
            "in her orbal research and isn't\x01",
            "getting any exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "She's so out of shape she'd probably\x01",
            "lose a shadow boxing match. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D14")

    label("loc_2CBB")

    OP_A2(0x2)

    ChrTalk(    #142
        0xFE,
        (
            "Hey! Did you hear about the\x01",
            "central factory?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "I really hope Louise is okay.\x02",
    )

    CloseMessageWindow()

    label("loc_2D14")

    Jump("loc_33E4")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E25")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2D7A")

    ChrTalk(    #144
        0xFE,
        "Grr, this is frustrating!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I hate it when we get a rush\x01",
            "for no reason!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2D7A")

    OP_A2(0x2)

    ChrTalk(    #146
        0xFE,
        (
            "Let's see. Saute's next...no, wait,\x01",
            "it was the soup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "When did all these dishes get\x01",
            "backed up like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Ben! We could really use your\x01",
            "help right now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E22")

    Jump("loc_33E4")

    label("loc_2E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2FB7")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2EFA")

    ChrTalk(    #149
        0xFE,
        (
            "Louise has been acting kind of\x01",
            "strange lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "She's hasn't been spending time\x01",
            "with her family, she hardly eats\x01",
            "at meals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "It's like she feels like she\x01",
            "doesn't have time for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB4")

    label("loc_2EFA")

    OP_A2(0x2)

    ChrTalk(    #152
        0xFE,
        (
            "That Louise. Who does she think\x01",
            "I am, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "'Oh, Ursus, can you take care of my\x01",
            "sister? I've got work,' she asks me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "Her job gives her more free\x01",
            "time than mine does!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB4")

    Jump("loc_33E4")

    label("loc_2FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_310B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_3021")

    ChrTalk(    #155
        0xFE,
        (
            "I'm really surprised I didn't\x01",
            "fall down the stairs there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "Lucky me, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3108")

    label("loc_3021")

    OP_A2(0x2)

    ChrTalk(    #157
        0xFE,
        (
            "I tell you, I couldn't believe\x01",
            "it yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I was bussing a table on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I was just coming down the\x01",
            "stairs when suddenly everything\x01",
            "went black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "I don't even know how I didn't\x01",
            "break the dishes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3108")

    Jump("loc_33E4")

    label("loc_310B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_326D")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_3180")

    ChrTalk(    #161
        0xFE,
        "Still...the recipe is really simple.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I'll try it out at my girlfriend's\x01",
            "house sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326A")

    label("loc_3180")

    OP_A2(0x2)

    ChrTalk(    #163
        0xFE,
        (
            "I know this soup looks a\x01",
            "little bit strange...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "...but when I actually tried it,\x01",
            "it was delicious! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Just throw it all in a pot and\x01",
            "warm it up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(    #166
        0xFE,
        "I'm impressed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "You're not just some lazy slug\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326A")

    Jump("loc_33E4")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33E4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(    #168
        0xFE,
        (
            "Seems like this soup can help\x01",
            "you concentrate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "...but I wonder if it really\x01",
            "does anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I mean, it's water, bouillon,\x01",
            "vegetables and pepper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_3321")

    OP_A2(0x2)

    ChrTalk(    #171
        0xFE,
        (
            "Let's see here...first the bouillon,\x01",
            "then the vegetables, and then a\x01",
            "dash of pepper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "Skim off the fat while it simmers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "What? Is that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "Seriously. Is that it?\x02",
    )

    CloseMessageWindow()

    label("loc_33E4")

    TalkEnd(0xFE)
    Return()

    # Function_14_28C2 end

    def Function_15_33E8(): pass

    label("Function_15_33E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3453")

    ChrTalk(    #176
        0xFE,
        "You're something else, Ben.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Looks like the only thing you\x01",
            "worked today is your jaw.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C36")

    label("loc_3453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_34F6")

    ChrTalk(    #178
        0xFE,
        (
            "Hoho! All that talk of new recipes\x01",
            "and hard work...and with a straight\x01",
            "face the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "That Ben really had me goin' there\x01",
            "for a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C36")

    label("loc_34F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_35F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3561")

    ChrTalk(    #180
        0xFE,
        (
            "Still though, I got so caught up\x01",
            "in the conversation I didn't notice\x01",
            "outside at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F5")

    label("loc_3561")

    OP_A2(0x3)

    ChrTalk(    #181
        0xFE,
        (
            "There used to be guys trying\x01",
            "to steal from the factory all\x01",
            "the time back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "I'd say they've refined their\x01",
            "methods these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F5")

    Jump("loc_3C36")

    label("loc_35F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_36D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_365F")

    ChrTalk(    #183
        0xFE,
        (
            "I think I'll tell young Ben about\x01",
            "that incident I had in the Ruan\x01",
            "souvenir shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D2")

    label("loc_365F")

    OP_A2(0x3)

    ChrTalk(    #184
        0xFE,
        (
            "Ha ha ha, workin's a job for\x01",
            "the young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "It does me good to see these\x01",
            "young folks all so hard at work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D2")

    Jump("loc_3C36")

    label("loc_36D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_378C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3738")

    ChrTalk(    #186
        0xFE,
        (
            "Hey, Ben! Is that saute ready\x01",
            "yet or not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "You've got customers waiting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3789")

    label("loc_3738")

    OP_A2(0x3)

    ChrTalk(    #188
        0xFE,
        (
            "I help out here when Ursus\x01",
            "isn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "The lunch rush is so busy!\x02",
    )

    CloseMessageWindow()

    label("loc_3789")

    Jump("loc_3C36")

    label("loc_378C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_380A")

    ChrTalk(    #190
        0xFE,
        "It's tough, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "I've been coming here so much\x01",
            "I'm sick of the food. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "I'd love something spicy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C36")

    label("loc_380A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_38F5")

    ChrTalk(    #193
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Everybody running around like\x01",
            "headless chickens just because\x01",
            "the orbments all went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "Try thinking about life before we had\x01",
            "them! Why, when I was young we...ah...\x01",
            "What were we talkin' about again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C36")

    label("loc_38F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39B8")
    OP_A2(0x577)

    ChrTalk(    #196
        0xFE,
        (
            "Gotta hand it to ol' Russell,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I was an old clockmaker,\x01",
            "right alongside him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "I had to retire because of my eyes,\x01",
            "but I sure hope Russell's a lifer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3D")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A38")

    ChrTalk(    #199
        0xFE,
        (
            "Sure, Ben's food is a bit simple,\x01",
            "but it tastes good enough, and\x01",
            "it's cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "One could say he's economical.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B3D")

    label("loc_3A38")

    OP_A2(0x3)

    ChrTalk(    #201
        0xFE,
        (
            "You need to watch yourself around\x01",
            "the owner, Ben.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "He loves to come up with all\x01",
            "kinds of justifications for his\x01",
            "plain cooking.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_69(0x9, 0x3E8)

    ChrTalk(    #203
        0x9,
        "HEY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x9,
        (
            "What are you telling my new\x01",
            "customers?!\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)

    ChrTalk(    #205
        0xFE,
        (
            "What?\x01",
            "I'm just tellin' it like it is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3D")

    Jump("loc_3C36")

    label("loc_3B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3BA5")

    ChrTalk(    #206
        0xFE,
        (
            "Yeah, I just got back from a\x01",
            "little trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "But it don't beat home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C36")

    label("loc_3BA5")

    OP_A2(0x3)

    ChrTalk(    #208
        0xFE,
        "Ahh, home at last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Yeah, I just got back from a\x01",
            "little trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I had a good time, but I sure am\x01",
            "glad to be back at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C36")

    TalkEnd(0xFE)
    Return()

    # Function_15_33E8 end

    def Function_16_3C3A(): pass

    label("Function_16_3C3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3CD9")

    ChrTalk(    #211
        0xFE,
        (
            "Lots of the food here is simple,\x01",
            "but it tastes good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "You can tell the cook here\x01",
            "doesn't want to spend his\x01",
            "time actually cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D74")

    label("loc_3CD9")

    OP_A2(0x0)

    ChrTalk(    #213
        0xFE,
        (
            "The hotel's kitchen is closed,\x01",
            "so I found this restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "In a town full of engineers,\x01",
            "the food's pretty simple.\x01",
            "But it's also pretty tasty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D74")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C3A end

    SaveToFile()

Try(main)
