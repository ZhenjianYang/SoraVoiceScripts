from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4270   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4270.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Queen Alicia',                         # 9
        'Duke Dunan',                           # 10
        'Butler Phillip',                       # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Shea',                                 # 16
        ' ',                                    # 17
        ' ',                                    # 18
        ' ',                                    # 19
        ' ',                                    # 20
        ' ',                                    # 21
        'Kloe',                                 # 22
        '1st Lieutenant Schwarz',               # 23
        'Head Maid Hilda',                      # 24
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH00000 ._CH',             # 03
        'ED6_DT07/CH00010 ._CH',             # 04
        'ED6_DT07/CH02010 ._CH',             # 05
        'ED6_DT07/CH02140 ._CH',             # 06
        'ED6_DT07/CH02470 ._CH',             # 07
        'ED6_DT07/CH01330 ._CH',             # 08
        'ED6_DT07/CH00100 ._CH',             # 09
        'ED6_DT07/CH00101 ._CH',             # 0A
        'ED6_DT07/CH00120 ._CH',             # 0B
        'ED6_DT07/CH00121 ._CH',             # 0C
        'ED6_DT07/CH00140 ._CH',             # 0D
        'ED6_DT07/CH00141 ._CH',             # 0E
        'ED6_DT07/CH02540 ._CH',             # 0F
        'ED6_DT07/CH00003 ._CH',             # 10
        'ED6_DT07/CH00013 ._CH',             # 11
        'ED6_DT07/CH02013 ._CH',             # 12
        'ED6_DT06/CH20020 ._CH',             # 13
        'ED6_DT07/CH00043 ._CH',             # 14
        'ED6_DT07/CH02093 ._CH',             # 15
        'ED6_DT07/CH02463 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH00000P._CP',             # 03
        'ED6_DT07/CH00010P._CP',             # 04
        'ED6_DT07/CH02010P._CP',             # 05
        'ED6_DT07/CH02140P._CP',             # 06
        'ED6_DT07/CH02470P._CP',             # 07
        'ED6_DT07/CH01330P._CP',             # 08
        'ED6_DT07/CH00100P._CP',             # 09
        'ED6_DT07/CH00101P._CP',             # 0A
        'ED6_DT07/CH00120P._CP',             # 0B
        'ED6_DT07/CH00121P._CP',             # 0C
        'ED6_DT07/CH00140P._CP',             # 0D
        'ED6_DT07/CH00141P._CP',             # 0E
        'ED6_DT07/CH02540P._CP',             # 0F
        'ED6_DT07/CH00003P._CP',             # 10
        'ED6_DT07/CH00013P._CP',             # 11
        'ED6_DT07/CH02013P._CP',             # 12
        'ED6_DT06/CH20020P._CP',             # 13
        'ED6_DT07/CH00043P._CP',             # 14
        'ED6_DT07/CH02093P._CP',             # 15
        'ED6_DT07/CH02463P._CP',             # 16
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638419,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1703955,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -103870,
        Z                   = 200,
        Y                   = 8990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -105240,
        Z                   = 200,
        Y                   = 7690,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -106560,
        Z                   = 200,
        Y                   = 8960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -1550,
        Range               = -2230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFF056,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = -1040,
        TriggerZ            = 8000,
        TriggerY            = 35960,
        TriggerRange        = 800,
        ActorX              = -1040,
        ActorZ              = 9000,
        ActorY              = 35960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_5BA",          # 01, 1
        "Function_2_624",          # 02, 2
        "Function_3_63A",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_6FB",          # 05, 5
        "Function_6_9A8",          # 06, 6
        "Function_7_AA1",          # 07, 7
        "Function_8_D06",          # 08, 8
        "Function_9_F1D",          # 09, 9
        "Function_10_111B",        # 0A, 10
        "Function_11_1712",        # 0B, 11
        "Function_12_5273",        # 0C, 12
        "Function_13_694B",        # 0D, 13
        "Function_14_69D3",        # 0E, 14
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3B4")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_3B4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C0"),
        (SWITCH_DEFAULT, "loc_3D6"),
    )


    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3")
    OP_A2(0x665)
    Event(0, 12)

    label("loc_3D3")

    Jump("loc_3D6")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    Jump("loc_40A")

    label("loc_3FB")

    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)

    label("loc_40A")

    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_4D6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 18)
    SetChrPos(0x8, -105250, 200, 10500, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, -104620, 640, 8950, 0)
    SetChrPos(0x12, -105280, 640, 8300, 0)
    SetChrPos(0x10, -105350, 640, 9620, 0)
    SetChrPos(0x13, -105990, 640, 8950, 0)
    SetChrPos(0x14, -105280, 700, 9050, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -107640, 0, 7110, 90)
    Jump("loc_522")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4FD")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53080, 0, 12340, 3)
    OP_43(0xF, 0x0, 0x0, 0x2)
    Jump("loc_522")

    label("loc_4FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_507")
    Jump("loc_522")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_511")
    Jump("loc_522")

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_51B")
    Jump("loc_522")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_522")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_52C")
    Jump("loc_5B9")

    label("loc_52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, -52830, 0, 7650, 179)
    SetChrPos(0xA, -53810, 0, 7520, 79)
    Jump("loc_5B9")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_5B9")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_5B9")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_580")
    Jump("loc_5B9")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_5B9")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_594")
    Jump("loc_5B9")

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5B9")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_5B9")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_5B2")
    Jump("loc_5B9")

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5B9")

    label("loc_5B9")

    Return()

    # Function_0_3A6 end

    def Function_1_5BA(): pass

    label("Function_1_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DE")
    OP_72(0x22, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_5DB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DB")

    Jump("loc_5EE")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_5EE")
    OP_71(0x22, 0x10)
    OP_64(0x0, 0x1)

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_60A")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_61A")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_61A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_5BA end

    def Function_2_624(): pass

    label("Function_2_624")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_639")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_624")

    label("loc_639")

    Return()

    # Function_2_624 end

    def Function_3_63A(): pass

    label("Function_3_63A")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "Duke Dunan is unconscious.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_63A end

    def Function_4_661(): pass

    label("Function_4_661")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xA,
        (
            "#720FYour Majesty...and everyone else,\x01",
            "as well... Thank you for showing\x01",
            "mercy.\x02\x03",

            "His Grace will surely remember\x01",
            "this kindness once he awakens.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_6FB(): pass

    label("Function_5_6FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_7F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_784")
    OP_A2(0x0)

    ChrTalk(    #2
        0xF,
        (
            "I helped the princess bake some\x01",
            "tasty desserts earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xF,
        (
            "They are scrumptious indeed!\x01",
            "Please, try some.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F5")

    label("loc_784")


    ChrTalk(    #4
        0xF,
        (
            "I helped the princess bake some\x01",
            "tasty desserts earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xF,
        (
            "They are scrumptious indeed!\x01",
            "Please, try some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F5")

    Jump("loc_9A4")

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_97F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_885")

    ChrTalk(    #6
        0xFE,
        (
            "The princess is currently roaming\x01",
            "the city incognito.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "She says that some...'school friends'\x01",
            "of hers are visiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97C")

    label("loc_885")

    OP_A2(0x0)

    ChrTalk(    #8
        0xFE,
        (
            "The princess has returned, so I am presently\x01",
            "cleaning her room...for a dirty room, you see,\x01",
            "is not very welcoming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "The princess is currently roaming\x01",
            "the city incognito.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "She says that some...'school friends'\x01",
            "of hers are visiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C")

    Jump("loc_9A4")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_989")
    Jump("loc_9A4")

    label("loc_989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_993")
    Jump("loc_9A4")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_99D")
    Jump("loc_9A4")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_9A4")

    label("loc_9A4")

    TalkEnd(0xFE)
    Return()

    # Function_5_6FB end

    def Function_6_9A8(): pass

    label("Function_6_9A8")

    TalkBegin(0x8)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9CD")
    SetChrSubChip(0xFE, 1)
    Jump("loc_9E8")

    label("loc_9CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E3")
    SetChrSubChip(0xFE, 0)
    Jump("loc_9E8")

    label("loc_9E3")

    SetChrSubChip(0xFE, 2)

    label("loc_9E8")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #11
        0x8,
        (
            "#090FMy, my, how long have I rested!\x02\x03",

            "There are so many things I must do...\x02\x03",

            "#094FIt seems I shall be forced to\x01",
            "part with my dearest Klaudia\x01",
            "again, as well...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_9A8 end

    def Function_7_AA1(): pass

    label("Function_7_AA1")

    TalkBegin(0x15)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC6")
    SetChrSubChip(0xFE, 2)
    Jump("loc_AF7")

    label("loc_AC6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ADC")
    SetChrSubChip(0xFE, 1)
    Jump("loc_AF7")

    label("loc_ADC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF2")
    SetChrSubChip(0xFE, 0)
    Jump("loc_AF7")

    label("loc_AF2")

    SetChrSubChip(0xFE, 2)

    label("loc_AF7")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B7C")

    ChrTalk(    #12
        0x15,
        (
            "#040FWhen you've finished what you're\x01",
            "doing, be sure to come back here\x01",
            "with Joshua.\x02\x03",

            "We can all take tea!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFD")

    label("loc_B7C")

    OP_A2(0x2)

    ChrTalk(    #13
        0x15,
        (
            "#040FEstelle, will you come take tea\x01",
            "with me?\x02\x03",

            "I just finished baking some tasty\x01",
            "treats to complement it. Perhaps\x01",
            "that will...sweeten the deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#506FI'm sorry, Kloe. I'm looking for\x01",
            "Joshua at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x15,
        (
            "#044FI see.\x02\x03",

            "#041FWell, if you find him, please bring\x01",
            "him as well, and we can all take tea\x01",
            "and dessert together!\x02\x03",

            "I'll be right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#008FUh...okay. Thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_CFD")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x15)
    Return()

    # Function_7_AA1 end

    def Function_8_D06(): pass

    label("Function_8_D06")

    TalkBegin(0x16)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D2B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D46")

    label("loc_D2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D41")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D46")

    label("loc_D41")

    SetChrSubChip(0xFE, 1)

    label("loc_D46")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E11")

    ChrTalk(    #17
        0x16,
        (
            "#170FWe won't let another Colonel Richard\x01",
            "rise to power ever again.\x02\x03",

            "#176FBetween the Royal Guardsmen, General\x01",
            "Morgan and Colonel Cassius, we'll make\x01",
            "sure to set things right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F14")

    label("loc_E11")

    OP_A2(0x3)

    ChrTalk(    #18
        0x16,
        (
            "#170FI'm so glad everything went smoothly\x01",
            "at the Queen's Birthday Celebration.\x02\x03",

            "We won't let another Colonel Richard\x01",
            "rise to power ever again.\x02\x03",

            "#176FBetween the Royal Guardsmen, General\x01",
            "Morgan and Colonel Cassius, we'll make\x01",
            "sure to set things right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F14")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x16)
    Return()

    # Function_8_D06 end

    def Function_9_F1D(): pass

    label("Function_9_F1D")

    TalkBegin(0x17)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F42")
    SetChrSubChip(0xFE, 1)
    Jump("loc_F73")

    label("loc_F42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F58")
    SetChrSubChip(0xFE, 2)
    Jump("loc_F73")

    label("loc_F58")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F6E")
    SetChrSubChip(0xFE, 0)
    Jump("loc_F73")

    label("loc_F6E")

    SetChrSubChip(0xFE, 1)

    label("loc_F73")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(    #19
        0x17,
        (
            "#711FWith Her Majesty and the princess\x01",
            "reunited, everything feels right\x01",
            "again... All in balance.\x02\x03",

            "And it's all thanks to you.\x02\x03",

            "I cannot express my gratitude\x01",
            "enough for all that you've done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1112")

    label("loc_104C")

    OP_A2(0x4)

    ChrTalk(    #20
        0x17,
        (
            "#711FWith Her Majesty and the princess\x01",
            "reunited, everything feels right\x01",
            "again... All in balance.\x02\x03",

            "And it's all thanks to you.\x02\x03",

            "I cannot express my gratitude\x01",
            "enough for all that you've done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1112")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x17)
    Return()

    # Function_9_F1D end

    def Function_10_111B(): pass

    label("Function_10_111B")

    EventBegin(0x0)
    OP_6D(-460, 0, 2620, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 10, 0, -5370, 225)
    SetChrPos(0x102, 10, 0, -5370, 225)
    SetChrPos(0x138, 10, 0, -5370, 225)

    def lambda_1197():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_1197)

    def lambda_11A9():
        OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0x564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_11A9)
    Sleep(500)

    def lambda_11C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11C9)

    def lambda_11DB():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11DB)
    Sleep(500)

    def lambda_11FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11FB)

    def lambda_120D():
        OP_8E(0xFE, 0x2EE, 0x0, 0xFFFFFE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_120D)
    WaitChrThread(0x138, 0x1)
    OP_8C(0x138, 180, 400)

    ChrTalk(    #21
        0x101,
        (
            "#327FWhew...\x01",
            "That was intense.\x02\x03",

            "#328FThanks, Hilda.\x01",
            "You're a real lifesaver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#331FYeah, that was really well done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x138,
        (
            "#713F#6PHa ha...\x01",
            "I'm just glad I could help.\x02\x03",

            "#711FNow, then... Are you planning\x01",
            "to change your clothes before\x01",
            "going to see Her Majesty?\x02\x03",

            "If you'd prefer, I can just\x01",
            "show you the way now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#471FI think I'm okay as-is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#333F#3SBoy clothes. Now.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)

    def lambda_13C4():
        OP_6D(7620, 0, 14990, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C4)
    OP_0D()
    OP_44(0x101, 0x1)
    SetMapFlags(0x800)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0x54)
    OP_6D(-52690, 0, 7170, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, -51850, 0, 7470, 270)
    SetChrPos(0x102, -53280, 0, 7850, 180)
    SetChrPos(0x138, -52990, 0, 5970, 0)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #26
        0x101,
        (
            "#4P#507FOh, for the love of... Why are\x01",
            "you always so self-conscious?\x02\x03",

            "What was wrong with what\x01",
            "you had on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#017FIt's not an issue of self-consciousness.\x02\x03",

            "#010FBy the way, Hilda. Is this\x01",
            "room what I think it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x138,
        (
            "#713FYes...\x01",
            "It is Princess Klaudia's bedroom.\x02\x03",

            "But she rarely sleeps in the\x01",
            "castle, so the room is all but\x01",
            "unused.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #29
        0x101,
        (
            "#501FHuh... No kidding?\x02\x03",

            "#505FBut I heard that the princess\x01",
            "was tending to the queen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x138,
        "#715F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#012FI guess that's just gossip, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x138,
        (
            "#713FYou'd have to ask Her Majesty\x01",
            "for the full details.\x02\x03",

            "#710FHer room is on the second\x01",
            "floor of the Royal Keep.\x02\x03",

            "I'll take you there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x643)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    Return()

    # Function_10_111B end

    def Function_11_1712(): pass

    label("Function_11_1712")

    EventBegin(0x0)
    Fade(1000)
    OP_A2(0x644)
    OP_28(0x4A, 0x1, 0x100)
    OP_28(0x4A, 0x1, 0x200)
    SetChrChipByIndex(0x138, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x138, -1000, 8000, 35250, 0)
    SetChrPos(0x101, -1500, 8000, 34000, 0)
    SetChrPos(0x102, -500, 8000, 34000, 0)
    SetChrPos(0x8, -980, 8000, 38840, 0)
    OP_6D(-1080, 8000, 35400, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(27000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x138,
        (
            "#713FI beg your pardon, Your Majesty.\x02\x03",

            "I've brought the two I spoke of\x01",
            "before. This is Joshua and Estelle.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #34
        0x8,
        "Elderly Woman's Voice",
        "#4PThank you kindly.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #35
        0x8,
        "Elderly Woman's Voice",
        "#4PBy all means, enter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x138,
        "#711FAs you wish.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x138, 270, 400)
    OP_8E(0x138, 0xFFFFF786, 0x1F40, 0x89B2, 0x7D0, 0x0)
    OP_8C(0x138, 180, 400)

    ChrTalk(    #37
        0x138,
        (
            "#711F#3PI'll wait for you here.\x02\x03",

            "You two go on in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#006FR-Right...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        "#015FPardon us...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-100970, 0, 4310, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -96900, 0, 15200, 0)
    SetChrPos(0x101, -101650, 0, 3300, 0)
    SetChrPos(0x102, -100450, 0, 3300, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #40
        0x101,
        "#004FOh...\x02",
    )

    CloseMessageWindow()

    def lambda_19A8():
        OP_6D(-97420, 0, 14400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19A8)

    def lambda_19C0():
        OP_6C(18000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19C0)

    def lambda_19D0():
        OP_67(0, 4200, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19D0)

    def lambda_19E8():
        OP_6E(317, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_19E8)
    Sleep(4000)
    OP_8C(0x8, 180, 300)

    ChrTalk(    #41
        0x8,
        (
            "#091F#6PHeehee...\x01",
            "I bid you welcome.\x02\x03",

            "#090FMy name is Alicia von Auslese.\x02\x03",

            "I am the twenty-sixth monarch\x01",
            "of the nation of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A8B():
        OP_6D(-97420, 0, 14400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A8B)

    def lambda_1AA3():
        OP_8E(0xFE, 0xFFFE7F32, 0x0, 0x3160, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA3)
    Sleep(300)

    def lambda_1AC3():
        OP_8E(0xFE, 0xFFFE8414, 0x0, 0x2F4E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AC3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #42
        0x101,
        (
            "#008FU-Umm... I'm Estelle Bright.\x02\x03",

            "I'm a junior bracer of the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#015FAnd I'm Joshua Bright, of\x01",
            "the same affiliation.\x02\x03",

            "It is a great honor to meet you,\x01",
            "Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#090F#6PEstelle and Joshua...\x02\x03",

            "I have truly been looking\x01",
            "forward to meeting you both.\x02\x03",

            "I regret that I cannot offer you\x01",
            "proper hospitality, but I have\x01",
            "prepared some tea.\x02\x03",

            "#091FPlease, have some and relax.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-105030, 0, 9180, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(1990, 0)
    OP_6C(44000, 0)
    OP_6E(368, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x102, 17)
    SetChrChipByIndex(0x8, 18)
    SetChrPos(0x8, -105250, 200, 10500, 180)
    SetChrPos(0x101, -103870, 200, 8990, 270)
    SetChrPos(0x102, -105250, 200, 7600, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x11, -104620, 640, 8950, 0)
    SetChrPos(0x12, -105280, 640, 8300, 0)
    SetChrPos(0x10, -105350, 640, 9620, 0)
    SetChrPos(0x14, -105280, 700, 9050, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #45
        0x8,
        (
            "#093FI see... So Professor Russell asked\x01",
            "you to bring this information...\x02\x03",

            "#094FA pitch-black orbment capable of\x01",
            "negating all other orbal energies...\x02\x03",

            "And you say that the colonel\x01",
            "has acquired it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#012FThe professor told us that you might\x01",
            "have some idea of what he intends to\x01",
            "do with it, Your Majesty.\x02\x03",

            "Can you tell us anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#094F...\x02\x03",

            "#093FI have but a vague idea...\x02\x03",

            "But I did not think that the\x01",
            "colonel even knew of it.\x02\x03",

            "Perhaps I am worrying about\x01",
            "nothing...but even so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#505FExcuse me...but what is\x01",
            "this vague idea you have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#094F...I suppose there is no\x01",
            "harm in telling you.\x02\x03",

            "#092FRoughly ten years ago, a massive orbal\x01",
            "reaction was detected beneath Grancel.\x02\x03",

            "Professor Russell was the individual\x01",
            "who came to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#004FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#012FDid this happen in the vicinity\x01",
            "of the sewers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#092FNo, far deeper underground\x01",
            "than that, in fact.\x02\x03",

            "Professor Russell was under the impression\x01",
            "that it might be a relic of the ancients\x01",
            "that still functioned.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #53
        0x101,
        "#004FWow...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(400)

    ChrTalk(    #54
        0x102,
        (
            "#012FSo...it was a bona fide artifact,\x01",
            "then?\x02\x03",

            "Most artifacts I know of have lost\x01",
            "their function, like the mechanisms\x01",
            "on top of the towers.\x02\x03",

            "But every now and again, you find\x01",
            "one that still functions--like\x01",
            "Mayor Dalmore's family heirloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#505FAnd something like that\x01",
            "is beneath Grancel...\x02\x03",

            "#580FSo, what does that tell\x01",
            "us about the Gospel...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(400)

    ChrTalk(    #56
        0x102,
        (
            "#012FMaybe...it could be used to halt\x01",
            "the artifact's functions?\x02\x03",

            "Could it do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#093FYes...\x02\x03",

            "However, we were unable to establish the nature\x01",
            "of the artifact, or indeed why it was buried\x01",
            "beneath the city.\x02\x03",

            "But it is beyond my imaginings how the colonel\x01",
            "could know of its existence...\x02\x03",

            "Professor Russell's research on it was kept\x01",
            "strictly confidential and off-the-record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013FI see...\x02\x03",

            "In any event, it seems likely\x01",
            "that trouble is on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#000FHonestly, just as I start to think maybe the\x01",
            "colonel might be a slightly nicer guy than we\x01",
            "were giving him credit for...\x02\x03",

            "#002FBut when someone's trying to stir up some\x01",
            "trouble, that's when us bracers come in!\x02\x03",

            "We won't let him get away with whatever evil\x01",
            "scheme he's trying to pull off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#090FHa ha...\x02\x03",

            "I'd expect no less from\x01",
            "Cassius' daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#004F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#014FYou're acquainted with our\x01",
            "father, Your Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#090FHe was a friend of my late son's, and a great\x01",
            "savior to the nation.\x02\x03",

            "Even after he retired from the army, he would\x01",
            "sometimes undertake requests for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#004FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#015FI didn't know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#090FHa ha... I imagine that there\x01",
            "are a great many things about\x01",
            "him that you do not know.\x02\x03",

            "Including the precise role\x01",
            "he played in the war, ten\x01",
            "years ago...\x02\x03",

            "I assume you have not been told?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#007FWell...\x01",
            "Nothing super-detailed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#094FPerhaps, then, that is the role\x01",
            "that I am meant to play...\x02\x03",

            "#090FEstelle and Joshua...\x02\x03",

            "Will you indulge me by\x01",
            "listening to an old story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#006FOh... Yes, absolutely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#010FIt is no indulgence, Your Majesty.\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_1D(0x53)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #71
        "\x07\x0CTen years ago, in the spring...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        "A tragedy occurred in the southern reaches of the Erebonian Empire...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        "Its cause is yet unknown, so that is something I must omit.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        "The Empire used that event as a pretext for their invasion of Liberl.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #75
        "So began the sad times that would become known as the Hundred Days War.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x4001B, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #76
        (
            "Just as the Empire made its declaration of war, a massive military force\x01",
            "breached the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #77
        (
            "In what seemed like scant moments, all of Liberl became occupied territory,\x01",
            "save for Grancel.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #78
        (
            "It is said that the invasion force was three times the size of the entire\x01",
            "Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #79
        "The reinforcements from Calvard were too late to stop their advance...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #80
        "It was but a matter of time before Grancel, too, would fall.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001C, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #81
        "But two months after the outbreak of hostilities...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #82
        "...the war changed in a way that none could have imagined.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #83
        (
            "Patrol airships had just been developed and were used to recapture Liberl's\x01",
            "checkpoints, severing the Imperial army's communications.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #84
        (
            "The Royal Army then set about recapturing the major regions one by one\x01",
            "using ships launched from Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #85
        "Zeiss, Ruan, Bose, Rolent...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #86
        (
            "With their supply lines severed, the Erebonian forces occupying each region\x01",
            "were swiftly crushed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001D, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #87
        (
            "And the one behind this plan for a counteroffensive was none other than\x01",
            "one Colonel Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "It was your father, who was General Morgan's right hand man at the time,\x01",
            "as well as Colonel Richard's superior officer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "Afterward, with the intercession of the Bracer Guild and the Septian Church,\x01",
            "the war was brought to an end.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        (
            "But it was at this time that Cassius lost what he treasured most in all the\x01",
            "world.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x4001E, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetChrName("Queen Alicia")

    AnonymousTalk(    #91
        "Lena...your mother, Estelle.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #92
        (
            "That clock tower was destroyed in the Imperial Army's vain attempts to hold\x01",
            "back the counteroffensive.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #93
        "What followed, I am sure you know.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #94
        "Cassius was not even able to be by his wife's side in her final moments...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #95
        0x101,
        (
            "#003FNo...\x02\x03",

            "I had no idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#094FAnd he believed that the military operation\x01",
            "that he himself had planned effectively caused\x01",
            "her death.\x02\x03",

            "Blaming himself, he left the military and took\x01",
            "up the path of the bracer.\x02\x03",

            "All to stay with the only one he had left:\x01",
            "you.\x02\x03",

            "And this time, he swore he would be able to\x01",
            "protect those he loved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#003FDad... That idiot...\x02\x03",

            "It wasn't his fault that Mom died...\x02\x03",

            "How could he even think that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        "#013FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#093FYes, you are correct...\x02\x03",

            "Given that all he lost was in\x01",
            "service to his country, the\x01",
            "responsibility falls upon me.\x02\x03",

            "#094FAnd so, I am sorry, Estelle...\x01",
            "I failed to protect your mother...\x02\x03",

            "I have wished to apologize\x01",
            "to you for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#002FB-But you don't need to apologize!\x02\x03",

            "#500FYou've protected the peace of this country ever\x01",
            "since the war ended.\x02\x03",

            "The peace that Dad and all the other soldiers\x01",
            "who defended Liberl in the war fought so hard\x01",
            "to protect...\x02\x03",

            "And the peace that Mom gave her life for so\x01",
            "I could live in it.\x02\x03",

            "#008FYou have nothing to be sorry for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#090FEstelle... You have a kind\x01",
            "heart, and I am grateful.\x02\x03",

            "#094FIt gladdens my heart to have\x01",
            "finally met you in person...\x02\x03",

            "Now, more than ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#008FYour Majesty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#094FHowever, that is why...\x02\x03",

            "#090FThat is why I do not wish you\x01",
            "to put yourself in danger.\x02\x03",

            "I would like for you to\x01",
            "remove yourself from any\x01",
            "dealings with this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#580FWha...!\x02\x03",

            "B-But Julia...I-I mean, Lieutenant\x01",
            "Schwarz...asked us to help you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "#090FI thank you. I am grateful for\x01",
            "your willingness to do so.\x02\x03",

            "But if some tragedy were to befall\x01",
            "you in Cassius' absence, I know of\x01",
            "no apology that could ever suffice.\x02\x03",

            "I ask only that you go back to\x01",
            "your home in Rolent and wait\x01",
            "for your father to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#580FB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#015FIf I may, Your Majesty...\x02\x03",

            "The peace that Dad restored and that\x01",
            "you protect, though it has held firm,\x01",
            "now trembles like a leaf in the breeze.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "#093FJoshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#012FIf the colonel is able to use the Gospel for\x01",
            "whatever purpose he intends...\x02\x03",

            "...and if he succeeds in making the duke the new\x01",
            "king of Liberl, then what will become of that\x01",
            "peace?\x02\x03",

            "I ask only that you consider that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        "#093F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#003FY-Your Majesty...?\x02\x03",

            "Right when we became junior\x01",
            "bracers, we inherited a whole\x01",
            "lot of work from Dad.\x02\x03",

            "After the sky bandit incident, we got that\x01",
            "letter and the package, and we've been\x01",
            "running all around creation ever since...\x02\x03",

            "It feels to us like our Dad's\x01",
            "been nudging us in the back\x01",
            "this whole time.\x02\x03",

            "#500FThat's why I want to defend peace...\x02\x03",

            "So that everyone we've met, and\x01",
            "everyone we care about...\x02\x03",

            "...can go on living secure\x01",
            "and happy lives.\x02\x03",

            "#002FJust like you...and just like Mom and Dad...\x01",
            "I'm doing this because it's what I believe is\x01",
            "right. And I really want to see it through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#093FEstelle...\x02\x03",

            "#094F...\x02\x03",

            "It seems...she was right\x01",
            "about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#090FI, too, am ready.\x02\x03",

            "I would like for the two of\x01",
            "you to carry my request to\x01",
            "the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#501FYour Majesty...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#010FMy Liege...\x01",
            "We will do whatever you ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#092FMy request is for the Bracer Guild to rescue\x01",
            "those being held captive by the Intelligence\x01",
            "Division.\x02\x03",

            "Amongst them is my granddaughter, Klaudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#002FAh-ha. So the princess IS being\x01",
            "held captive somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "#094FYes...\x02\x03",

            "This coup d'etat started when\x01",
            "I backed her as the successor\x01",
            "to the throne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        (
            "#012FIn other words, Duke Dunan\x01",
            "was out of the running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "#093FYes... Though he is my nephew,\x01",
            "he is possessed of a considerable\x01",
            "number of character flaws.\x02\x03",

            "In brief, where he is lacking,\x01",
            "my granddaughter shines.\x02\x03",

            "For the sake of this nation's\x01",
            "future, I would have my\x01",
            "granddaughter succeed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#506FWell...um, I don't actually\x01",
            "know her...\x02\x03",

            "But I personally lean toward the\x01",
            "idea that your judgment should\x01",
            "REALLY be trusted here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#094FNo matter the era, there will always be\x01",
            "those who object strongly to a woman\x01",
            "wielding political power.\x02\x03",

            "Not to mention, the memory of\x01",
            "the invasion by a larger power\x01",
            "is still relatively fresh...\x02\x03",

            "#092FSome of them will perceive a\x01",
            "succession of two consecutive\x01",
            "queens to be a sign of weakness.\x02\x03",

            "It is hardly surprising that\x01",
            "such a notion has taken root\x01",
            "in the minds of some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#015F'Some' including Colonel Richard,\x01",
            "I presume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#092FQuite right.\x02\x03",

            "Klaudia's pending succession to the\x01",
            "throne caught him quite unawares.\x02\x03",

            "That, along with his passing of\x01",
            "this information to the duke, is what\x01",
            "led to this coup.\x02\x03",

            "This was all staged so that Liberl would\x01",
            "become a strong military power, with\x01",
            "the colonel ruling from the shadows...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#012FI see...\x02\x03",

            "That finally lets us see\x01",
            "the whole picture.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #127
        0x101,
        (
            "#505FSo if Liberl became a militarized\x01",
            "country...what would happen then?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)
    Sleep(400)

    ChrTalk(    #128
        0x102,
        (
            "#012FA great many things.\x02\x03",

            "Taxes would be levied to fill the war chest...\x02\x03",

            "Orbal weaponry would be developed with the\x01",
            "express intent of causing havoc on a massive\x01",
            "scale...\x02\x03",

            "A wide-ranging policy of conscription\x01",
            "would be adopted...\x02\x03",

            "And no doubt contracting jaeger corps would\x01",
            "be made legal, which is not the case at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#580FOh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#094FIndeed, the colonel has made\x01",
            "very adamant requests that I\x01",
            "enact such policies.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(400)

    ChrTalk(    #131
        0x8,
        (
            "#093FI thought that such proposals were\x01",
            "born out of genuine love for his country...\x02\x03",

            "...but I never agreed that they were the\x01",
            "right course of action to take.\x02\x03",

            "The Royal Army is not all that protects\x01",
            "this land.\x02\x03",

            "We have worked hard to maintain treaties\x01",
            "with other countries.\x02\x03",

            "Defending a nation goes hand in hand with\x01",
            "free cultural exchange and trade with all\x01",
            "other nations, to the benefit of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        "#015FI feel the same way, Your Majesty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#006FYeah! Makes sense to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#092FThe colonel, however, finds such notions to\x01",
            "be womanly and foolishly idealistic.\x02\x03",

            "And so he demanded that I abdicate the throne\x01",
            "in exchange for Klaudia's safe return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#005F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#094FMany people have had family members\x01",
            "taken to ensure that they would\x01",
            "not dare to oppose the colonel.\x02\x03",

            "But I am the queen. And I will not allow\x01",
            "all that I love about my country to be\x01",
            "destroyed, simply because of blood ties.\x02\x03",

            "#093FStill...she is my only granddaughter...\x02\x03",

            "I cannot simply allow her to die...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#006FYour Majesty...please try to relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        (
            "#010FWe hear and comply with\x01",
            "your request.\x02\x03",

            "We will see to it that the princess\x01",
            "is rescued from those who have\x01",
            "imprisoned her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "#090FThank you...both of you.\x02\x03",

            "With that reassurance, I will do all I can\x01",
            "to oppose the colonel's demands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#002FU-Umm... H-Have you any other\x01",
            "requests, Your Majesty?\x02\x03",

            "The Gospel still has\x01",
            "to be dealt with...\x02\x03",

            "And I don't think we should\x01",
            "just leave you here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "#090FI appreciate your sentiment, Estelle.\x02\x03",

            "But the present state of affairs\x01",
            "is not contingent upon my freedom\x01",
            "or imprisonment.\x02\x03",

            "#094FThe Gospel shall continue to weigh\x01",
            "heavily on my mind, for a great\x01",
            "many reasons...\x02\x03",

            "For my part, I will attempt to\x01",
            "ascertain the colonel's true\x01",
            "intentions with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_6D(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x138, 0)
    SetChrPos(0x101, -53000, 0, 6160, 90)
    SetChrPos(0x102, -51450, 0, 6000, 270)
    OP_1D(0x54)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #142
        0x101,
        (
            "#328F*sigh*... Wow, what a totally\x01",
            "awesome person.\x02\x03",

            "Super-nice, but with a\x01",
            "seriously strong will.\x02\x03",

            "#321FI hope I'm even one-tenth\x01",
            "that cool when I get old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        (
            "#337F'Cool.' Did you actually just\x01",
            "call the queen that?\x02\x03",

            "#338FStill, she definitely has what it\x01",
            "takes to govern a whole country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#323FYeah...\x02\x03",

            "I really want to stop this\x01",
            "coup thingy and help her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#330FThat's definitely outside\x01",
            "of bracer jurisdiction.\x02\x03",

            "Well, first things first.\x01",
            "We do whatever we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#326FRight.\x02\x03",

            "#327FBut you know, I'm still freaking\x01",
            "out about what the queen told\x01",
            "us about Dad.\x02\x03",

            "I wonder if she's got any more\x01",
            "tidbits she'd be willing to share...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x138, -51030, 0, 420, 225)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4FE5():

        label("loc_4FE5")

        TurnDirection(0xFE, 0x138, 400)
        OP_48()
        Jump("loc_4FE5")

    QueueWorkItem2(0x101, 1, lambda_4FE5)

    def lambda_4FF6():

        label("loc_4FF6")

        TurnDirection(0xFE, 0x138, 400)
        OP_48()
        Jump("loc_4FF6")

    QueueWorkItem2(0x102, 1, lambda_4FF6)

    ChrTalk(    #147
        0x138,
        (
            "#1PEstelle and Joshua...\x02\x03",

            "Have you finished changing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5042():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5042)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #148
        0x101,
        "#471FOh, yeah.\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_5075():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_5075)

    def lambda_5087():
        OP_8E(0xFE, 0xFFFF34A4, 0x0, 0xF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_5087)
    OP_6D(-52330, 0, 5310, 2000)
    WaitChrThread(0x138, 0x1)

    ChrTalk(    #149
        0x138,
        (
            "#710FThen we should return to\x01",
            "the waiting room at once.\x02\x03",

            "It's already after eleven o'clock.\x01",
            "Actually, it's almost midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#324FWhoa...\x01",
            "Is it really that late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#330FThe Queen spoke with\x01",
            "us for a long time.\x02\x03",

            "If we stay any longer, it's apt\x01",
            "to make the guards suspicious.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x101, -52650, 0, 5460, 180)
    SetChrPos(0x102, -52650, 0, 5460, 180)
    SetChrPos(0x138, -52650, 0, 5460, 180)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    OP_1B(0x2, 0x0, 0xFFFF)
    OP_6D(-52650, 0, 5460, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_1712 end

    def Function_12_5273(): pass

    label("Function_12_5273")

    OP_28(0x4E, 0x1, 0x4)
    EventBegin(0x0)
    OP_6D(170, 0, 5170, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 0, 0, 9760, 180)
    SetChrPos(0xB, -1480, 0, 9280, 180)
    SetChrPos(0xC, -660, 0, 8290, 180)
    SetChrPos(0xD, 700, 0, 8420, 180)
    SetChrPos(0xE, 1400, 0, 9310, 180)
    SetChrPos(0x101, -90, 0, 920, 0)
    SetChrPos(0x105, -1330, 0, 430, 0)
    SetChrPos(0x103, 930, 0, 430, 0)
    SetChrChipByIndex(0x101, 9)
    SetChrChipByIndex(0x103, 11)
    SetChrChipByIndex(0x105, 13)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #152
        0x9,
        (
            "#220FTr-Traitors!\x01",
            "You dare to come here?!\x02\x03",

            "Do you not realize that\x01",
            "I am the new king?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#000FOh, go brush your goofy hairdo.\x02\x03",

            "You ain't king YET.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        "#220FWH-WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#020FYour Grace, Duke Dunan.\x01",
            "We are with the Bracer Guild.\x02\x03",

            "At the request of Her Highness, \x01",
            "Princess Klaudia, we are here \x01",
            "to free the queen!\x02\x03",

            "It would be best for all involved\x01",
            "if you quietly stood aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        (
            "#220FK-Klaudia?!\x02\x03",

            "Damn that brat!\x01",
            "Damn her to hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x105,
        (
            "#040FUncle Dunan...please, stop this.\x02\x03",

            "Colonel Richard is just using you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x9,
        (
            "#220FWha... Who are you...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #159
        0x9,
        (
            "#220FK-K-K-Klaudia, is that you?!\x02\x03",

            "What happened to your hair?!\x01",
            "And your clothes?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#000FWe have comprehension! \x01",
            "Repeat, we have comprehension!\x02\x03",

            "Though he still hasn't noticed\x01",
            "that we first met him in Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x103,
        (
            "#020FNo idea what you're talking\x01",
            "about...but he doesn't seem\x01",
            "the most observant sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        (
            "#040FI was wrong to keep silent,\x01",
            "I think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "#220FH-How dare you make\x01",
            "a fool of me?!\x02\x03",

            "It's because of things like this that\x01",
            "those creatures known as 'women'\x01",
            "are not to be trusted!\x02\x03",

            "Sly, narrow-minded, nit-picking,\x01",
            "nagging wretches...\x02\x03",

            "How could I ever give up the\x01",
            "crown to such a vile creature?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        "#020F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x105,
        "#040F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #167
        0x9,
        "#220F...Err... I mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xB,
        (
            "Y-Your Grace... I don't think\x01",
            "that was the right thing to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xC,
        "M-Maybe you should apologize...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#000FHmmm...\x01",
            "'Vile creatures,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#020FMy, my. I believe you've just\x01",
            "gone from stupid to suicidal.\x02\x03",

            "After all, that's a mighty courageous\x01",
            "sentiment to vocalize when in the\x01",
            "presence of three ARMED women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x105,
        (
            "#040FI... I'm sorry, Uncle.\x02\x03",

            "In this, I cannot defend you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A6A():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A6A)

    def lambda_5A85():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A85)

    def lambda_5AA0():
        OP_8E(0xFE, 0x122, 0x0, 0x59A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AA0)
    OP_6D(420, 0, 10250, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    Battle(0x3AA, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5AEB"),
        (SWITCH_DEFAULT, "loc_5AEE"),
    )


    label("loc_5AEB")

    OP_B4(0x0)
    Return()

    label("loc_5AEE")

    EventBegin(0x0)
    SetChrPos(0xB, -1890, 0, 12000, 315)
    SetChrPos(0xC, 280, 0, 13640, 135)
    SetChrPos(0xD, 3410, 0, 11230, 315)
    SetChrPos(0xE, 1760, 0, 8900, 177)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (3, "loc_5B40"),
        (SWITCH_DEFAULT, "loc_6344"),
    )


    label("loc_5B40")

    OP_6D(-2350, 0, 8189, 0)
    SetChrPos(0x9, -4620, 0, 7950, 90)
    SetChrPos(0x101, -1690, 0, 9010, 22)
    SetChrPos(0x105, -390, 0, 8010, 90)
    SetChrPos(0x103, -1510, 0, 6870, 90)
    OP_2B(0x4D, 0x2)

    ChrTalk(    #173
        0x101,
        (
            "#000FWell, that settles that!\x02\x03",

            "Now, then, shall I show you just\x01",
            "how 'vile' a woman can be?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C00():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C00)

    def lambda_5C0E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C0E)

    def lambda_5C1C():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C1C)
    OP_8F(0x9, 0xFFFFEAC0, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(    #174
        0x103,
        (
            "#020FMaybe I should give him a taste\x01",
            "of a ladylike whipping.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x9, 0xFFFFE6E2, 0x0, 0x1EB4, 0x7D0, 0x0)

    ChrTalk(    #175
        0x9,
        (
            "#220FEe...eeeeeeeeep...\x02\x03",

            "S-Stay back!\x01",
            "Please, stay awaaay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        (
            "#040FUm... I might be able\x01",
            "to call them off...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D08():
        OP_6D(-4750, 0, 8080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D08)

    ChrTalk(    #177
        0x9,
        (
            "#220FI-If you do, I swear I'll be Her Majesty's\x01",
            "very own human shield!\x02\x03",

            "AAAIEEEE! MOMMY!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D7E():
        OP_8C(0xFE, 275, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D7E)
    OP_8F(0x9, 0xFFFFDFD0, 0x0, 0x1E82, 0x1B58, 0x0)
    OP_62(0x9, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)

    def lambda_5DB7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DB7)
    OP_8F(0x9, 0xFFFFE124, 0x0, 0x1E82, 0xBB8, 0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_5DDE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DDE)

    ChrTalk(    #178
        0x9,
        "#220FHurrrrk...buurrrgggle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#000FOops... Maybe we overdid\x01",
            "it with the threats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#020FWell, a little dose of the cold,\x01",
            "hard truth might be the best\x01",
            "medicine he ever gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#040FYes... It is an unfortunate situation\x01",
            "he's gotten himself into.\x02\x03",

            "Still, I cannot allow my unconscious\x01",
            "uncle to simply be lef--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -50, 0, 340, 315)

    ChrTalk(    #182
        0xA,
        "...Y-Your Grace?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_5F6B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F6B)

    def lambda_5F79():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F79)

    def lambda_5F87():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F87)
    OP_6D(-2009, 0, 6520, 1000)

    def lambda_5FA6():

        label("loc_5FA6")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FA6")

    QueueWorkItem2(0x101, 1, lambda_5FA6)

    def lambda_5FB7():

        label("loc_5FB7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FB7")

    QueueWorkItem2(0x103, 1, lambda_5FB7)

    def lambda_5FC8():

        label("loc_5FC8")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_5FC8")

    QueueWorkItem2(0x105, 1, lambda_5FC8)

    def lambda_5FD9():
        OP_6D(-4750, 0, 8080, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FD9)
    OP_92(0xA, 0x9, 0x258, 0x1388, 0x0)

    ChrTalk(    #183
        0x101,
        "#000FHi, Phillip!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #184
        0xA,
        (
            "#720FMiss Estelle...and Your Highness?!\x02\x03",

            "I can offer no words to make\x01",
            "up for my master's behavior\x01",
            "in this instance!\x02\x03",

            "As the man who raised him,\x01",
            "the responsibility is mine\x01",
            "to bear!\x02\x03",

            "Please, I ask that you \x01",
            "punish me in his stead!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #185
        "\x07\x05Phillip bowed his head deeply.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #186
        0x101,
        (
            "#000FP-Punish...? We didn't knock\x01",
            "him out... He just fainted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        (
            "#040FPlease, Phillip...\x01",
            "Lift your eyes.\x02\x03",

            "We're here to help my grandmother...\x01",
            "to save the queen.\x02\x03",

            "We have no intention of\x01",
            "doing anything to the duke.\x02\x03",

            "I would appreciate it if you\x01",
            "would take him to my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "#720FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x103,
        (
            "#020FHe's not actually hurt.\x02\x03",

            "He just passed out from the shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "#720FTh-Thank you so much...\x01",
            "All of you...\x02\x03",

            "I will not forget the boon\x01",
            "you've granted!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_63(0x9)
    FadeToBright(2000, 0)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    EventEnd(0x0)
    Return()

    label("loc_6344")

    OP_6D(370, 0, 8590, 0)
    SetChrPos(0x9, 1620, 0, 8100, 112)
    SetChrPos(0x101, -1690, 0, 9010, 22)
    SetChrPos(0x105, -390, 0, 8010, 90)
    SetChrPos(0x103, -1510, 0, 6870, 90)
    TurnDirection(0x101, 0x9, 0)
    TurnDirection(0x105, 0x9, 0)
    TurnDirection(0x103, 0x9, 0)

    ChrTalk(    #191
        0x101,
        (
            "#000FWhew... I thought he was going\x01",
            "to go belly-up on us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x103,
        (
            "#020FI really only wanted to beat on\x01",
            "the Special Ops soldiers...\x02\x03",

            "Well, a little dose of the cold,\x01",
            "hard truth might be the best\x01",
            "medicine he ever gets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x105,
        (
            "#040FBut a little dose of the cold,\x01",
            "hard truth might be the best\x01",
            "medicine he ever gets.\x02\x03",

            "Still, I cannot allow my unconscious\x01",
            "uncle to simply be lef--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -120, 0, -820, 315)

    ChrTalk(    #194
        0xA,
        "...Y-Your Grace?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x105, 65535)

    def lambda_656C():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_656C)

    def lambda_657A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_657A)

    def lambda_6588():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6588)
    OP_6D(510, 0, 4400, 1000)

    def lambda_65A7():

        label("loc_65A7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65A7")

    QueueWorkItem2(0x101, 1, lambda_65A7)

    def lambda_65B8():

        label("loc_65B8")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65B8")

    QueueWorkItem2(0x103, 1, lambda_65B8)

    def lambda_65C9():

        label("loc_65C9")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_65C9")

    QueueWorkItem2(0x105, 1, lambda_65C9)

    def lambda_65DA():
        OP_6D(370, 0, 8590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_65DA)
    OP_92(0xA, 0x9, 0x258, 0x1388, 0x0)

    ChrTalk(    #195
        0x101,
        "#000FHi, Phillip!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #196
        0xA,
        (
            "#720FMiss Estelle...and Your Highness?!\x02\x03",

            "I can offer no words to make\x01",
            "up for my master's behavior\x01",
            "in this instance!\x02\x03",

            "As the man who raised him,\x01",
            "the responsibility is mine\x01",
            "to bear!\x02\x03",

            "Please, I ask that you \x01",
            "punish me in his stead!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #197
        "\x07\x05Phillip bowed his head deeply.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #198
        0x101,
        "#000FH-Hey! Hold on a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x105,
        (
            "#040FPlease, Phillip...\x01",
            "Lift your eyes.\x02\x03",

            "We're here to help my grandmother...\x01",
            "to save the queen.\x02\x03",

            "We have no intention of\x01",
            "doing anything to the duke.\x02\x03",

            "I would appreciate it if you\x01",
            "would take him to my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        "#720FY-Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x103,
        (
            "#020FHe's not actually hurt.\x02\x03",

            "It was just shock at the thought\x01",
            "of someone actually laying a\x01",
            "hand on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xA,
        (
            "#720FTh-Thank you so much...\x01",
            "All of you...\x02\x03",

            "I will not forget the boon\x01",
            "you've granted!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_63(0x9)
    FadeToBright(2000, 0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_12_5273 end

    def Function_13_694B(): pass

    label("Function_13_694B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69D2")
    EventBegin(0x1)
    TurnDirection(0x0, 0x1, 400)

    NpcTalk(    #203
        0x0,
        "Head Maid Hilda",
        (
            "#710FHer Majesty's room is on the second\x01",
            "floor of the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_69D2")

    Return()

    # Function_13_694B end

    def Function_14_69D3(): pass

    label("Function_14_69D3")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_14_69D3 end

    SaveToFile()

Try(main)
