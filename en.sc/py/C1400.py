from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1400   ._SN',
        MapName             = 'Bose',
        Location            = 'C1400.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        '',                                     # 9
        'Whemler',                              # 10
        'Sieg',                                 # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT09/CH11170 ._CH',             # 00
        'ED6_DT09/CH11171 ._CH',             # 01
        'ED6_DT09/CH11180 ._CH',             # 02
        'ED6_DT09/CH11181 ._CH',             # 03
        'ED6_DT09/CH11190 ._CH',             # 04
        'ED6_DT09/CH11191 ._CH',             # 05
        'ED6_DT09/CH10170 ._CH',             # 06
        'ED6_DT09/CH10171 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT07/CH01680 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT26/CH20238 ._CH',             # 0D
        'ED6_DT06/CH20051 ._CH',             # 0E
        'ED6_DT26/CH20254 ._CH',             # 0F
        'ED6_DT07/CH01660 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH11170P._CP',             # 00
        'ED6_DT09/CH11171P._CP',             # 01
        'ED6_DT09/CH11180P._CP',             # 02
        'ED6_DT09/CH11181P._CP',             # 03
        'ED6_DT09/CH11190P._CP',             # 04
        'ED6_DT09/CH11191P._CP',             # 05
        'ED6_DT09/CH10170P._CP',             # 06
        'ED6_DT09/CH10171P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT07/CH01680P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT26/CH20238P._CP',             # 0D
        'ED6_DT06/CH20051P._CP',             # 0E
        'ED6_DT26/CH20254P._CP',             # 0F
        'ED6_DT07/CH01660P._CP',             # 10
    )

    DeclNpc(
        X                   = -42410,
        Z                   = 4019,
        Y                   = 103940,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -68750,
        Z                   = 50,
        Y                   = 92910,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -112800,
        Z                   = -50,
        Y                   = 104070,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86000,
        Z                   = 2020,
        Y                   = 104050,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91980,
        Z                   = 2080,
        Y                   = 122080,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78470,
        Z                   = 4059,
        Y                   = 133110,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61710,
        Z                   = 4050,
        Y                   = 112490,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46460,
        Z                   = 4080,
        Y                   = 83320,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -42410,
        Y                   = 3500,
        Z                   = 103940,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -43500,
        Y                   = 3500,
        Z                   = 104740,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -67400,
        Y                   = 3000,
        Z                   = 184200,
        Range               = -60300,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x2D2A8,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -78820,
        TriggerZ            = 90,
        TriggerY            = 98230,
        TriggerRange        = 1000,
        ActorX              = -78790,
        ActorZ              = 1590,
        ActorY              = 97650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -85490,
        TriggerZ            = -30,
        TriggerY            = 115790,
        TriggerRange        = 1000,
        ActorX              = -85380,
        ActorZ              = 1200,
        ActorY              = 115700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_354",          # 01, 1
        "Function_2_3F0",          # 02, 2
        "Function_3_406",          # 03, 3
        "Function_4_41F",          # 04, 4
        "Function_5_509",          # 05, 5
        "Function_6_64F",          # 06, 6
        "Function_7_987",          # 07, 7
        "Function_8_16CA",         # 08, 8
        "Function_9_1965",         # 09, 9
        "Function_10_1D68",        # 0A, 10
        "Function_11_2B81",        # 0B, 11
        "Function_12_2C7F",        # 0C, 12
        "Function_13_2D08",        # 0D, 13
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    OP_11(0xFF, 0xFF, 0xFF, 0x80E8, 0xE290, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_315")

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_END)), "loc_332")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -42100, 4000, 104960, 135)

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_END)), "loc_33E")
    SetChrFlags(0x9, 0x80)

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_353")

    Return()

    # Function_0_2FE end

    def Function_1_354(): pass

    label("Function_1_354")

    OP_C4(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    OP_6F(0x2, 0)
    Jump("loc_373")

    label("loc_36C")

    OP_6F(0x2, 60)

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0x6, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0x6, 60)

    label("loc_38C")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CD")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_END)), "loc_3DE")
    OP_72(0x1, 0x4)
    OP_71(0x3, 0x4)

    label("loc_3DE")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_354 end

    def Function_2_3F0(): pass

    label("Function_2_3F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F0")

    label("loc_405")

    Return()

    # Function_2_3F0 end

    def Function_3_406(): pass

    label("Function_3_406")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x9,
        "◆セリフ無し\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_406 end

    def Function_4_41F(): pass

    label("Function_4_41F")

    OP_EA(0x2, 0x53, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x1, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found #2C#57IWater Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B14)
    Jump("loc_4F7")

    label("loc_49A")


    AnonymousTalk(    #2
        (
            "\x07\x05There is nothing in the chest but spiders now.\x01",
            "They all stare at you and clap. Bravo.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4F7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_41F end

    def Function_5_509(): pass

    label("Function_5_509")

    OP_EA(0x2, 0x54, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_57A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xD9\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B15)
    Jump("loc_5DE")

    label("loc_57A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xD9\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD9\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_5DE")

    Jump("loc_641")

    label("loc_5E1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You're not diggin this whole 'one item per chest'\x01",
            "thing, are you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_641")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_509 end

    def Function_6_64F(): pass

    label("Function_6_64F")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave Alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6CB"),
        (1, "loc_91C"),
        (SWITCH_DEFAULT, "loc_984"),
    )


    label("loc_6CB")

    Battle(0xBB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6EC"),
        (2, "loc_89C"),
        (1, "loc_914"),
        (SWITCH_DEFAULT, "loc_919"),
    )


    label("loc_6EC")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Set as exterminated the wanted monsters at the Amberl Tower and Krone Pass.\x01",      # 0
            "No change\x01",                                                                        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_790"),
        (SWITCH_DEFAULT, "loc_7A5"),
    )


    label("loc_790")

    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0xB3, 0x1, 0x1)
    Jump("loc_7A5")

    label("loc_7A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B7")
    Call(0, 7)
    Jump("loc_899")

    label("loc_7B7")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40990, 3930, 102060, 315)
    SetChrPos(0x1, -40990, 3930, 102060, 315)
    SetChrPos(0x2, -40990, 3930, 102060, 315)
    SetChrPos(0x3, -40990, 3930, 102060, 315)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Exterminated monster in Nebel Valley!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x80)
    OP_28(0x93, 0x1, 0x100)
    OP_28(0x93, 0x1, 0x200)
    Sleep(400)

    label("loc_899")

    Jump("loc_919")

    label("loc_89C")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40390, 3880, 100330, 315)
    SetChrPos(0x1, -40390, 3880, 100330, 315)
    SetChrPos(0x2, -40390, 3880, 100330, 315)
    SetChrPos(0x3, -40390, 3880, 100330, 315)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_919")

    label("loc_914")

    OP_B4(0x0)
    Jump("loc_919")

    label("loc_919")

    Jump("loc_984")

    label("loc_91C")

    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40390, 3880, 100330, 315)
    SetChrPos(0x1, -40390, 3880, 100330, 315)
    SetChrPos(0x2, -40390, 3880, 100330, 315)
    SetChrPos(0x3, -40390, 3880, 100330, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    Jump("loc_984")

    label("loc_984")

    EventEnd(0x0)
    Return()

    # Function_6_64F end

    def Function_7_987(): pass

    label("Function_7_987")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99A")
    Call(0, 11)

    label("loc_99A")

    OP_6D(-42350, 4059, 103640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -41720, 3990, 104460, 225)
    SetChrPos(0x106, -43170, 4059, 104220, 135)
    SetChrPos(0xF8, -41440, 4030, 102690, 315)
    SetChrPos(0xF9, -42900, 4070, 102590, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        (
            "#1007FPhew! That's the last one.\x02\x03",

            "#1002FStill, though.\x01",
            "Didn't they seem kind of odd?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x18\x07\x05What seemed odd about the monsters?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "The Monsters Were Strong\x01",        # 0
            "The Monsters Were Afraid\x01",        # 1
            "The Monsters Were Agitated\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B5E"),
        (1, "loc_DF6"),
        (2, "loc_1049"),
        (SWITCH_DEFAULT, "loc_129C"),
    )


    label("loc_B5E")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFA")

    ChrTalk(    #10
        0x108,
        (
            "#072FIt was a challenge, but...\x01",
            "the monsters' behavior was odd, as well.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DED")

    label("loc_BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(    #11
        0x103,
        (
            "#022FThat's definitely true, but...\x01",
            "it also felt like they were acting\x01",
            "very strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DED")

    label("loc_CA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D48")

    ChrTalk(    #12
        0x104,
        (
            "#032FPerhaps. But there seemed to be\x01",
            "more to it.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DED")

    label("loc_D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DED")

    ChrTalk(    #13
        0x105,
        (
            "#043FThey were certainly powerful,\x01",
            "but their behavior... It was so odd.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DED")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_129C")

    label("loc_DF6")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E73")

    ChrTalk(    #14
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1040")

    label("loc_E73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF7")

    ChrTalk(    #15
        0x103,
        (
            "#022FYes, all of the monsters were acting\x01",
            "strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1040")

    label("loc_EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAC")

    ChrTalk(    #16
        0x104,
        (
            "#032FHmm. Yes, their behavior was,\x01",
            "unusual, to say the least.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1040")

    label("loc_FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1040")

    ChrTalk(    #17
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1040")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_129C")

    label("loc_1049")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(    #18
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_10C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #19
        0x103,
        (
            "#022FYes, all of the monsters were acting strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_114A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FF")

    ChrTalk(    #20
        0x104,
        (
            "#032FHmm. Yes, their behavior was,\x01",
            "to say the least, unusual.\x02\x03",

            "Some bared their fangs at us in fury,\x01",
            "others were ready to flee from us like\x01",
            "scared children...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1293")

    label("loc_11FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(    #21
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1293")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_129C")

    label("loc_129C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12ED")

    ChrTalk(    #22
        0x107,
        (
            "#065FI kinda noticed that too.\x02\x03",

            "#561FIt was kinda scary...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FC")

    label("loc_12ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #23
        0x105,
        (
            "#043FI also noticed that.\x02\x03",

            "I wonder what it could mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FC")

    label("loc_133B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A7")

    ChrTalk(    #24
        0x104,
        (
            "#032FI, too, could not help but notice\x01",
            "their confusion.\x02\x03",

            "I wish I knew what it meant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FC")

    label("loc_13A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FC")

    ChrTalk(    #25
        0x103,
        (
            "#026FI got the same impression.\x02\x03",

            "#522FMmmm... What could it mean?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FC")


    ChrTalk(    #26
        0x106,
        "#057F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004FAgate? Something up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#555FEh...\x02\x03",

            "Just thinkin' this might be a warning\x01",
            "about somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1020FA warning... You mean to something\x01",
            "Ouroboros is doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x106,
        (
            "#552FI can't say for sure, but...somethin'\x01",
            "like this has happened before.\x02\x03",

            "Day after day, the monsters were all\x01",
            "riled up.\x02\x03",

            "And then, bam, right after that...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004FRight after...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(    #32
        0x107,
        "#063FAgate...?\x02",
    )

    CloseMessageWindow()

    label("loc_159A")


    ChrTalk(    #33
        0x106,
        (
            "#053FEnough 'bout that.\x02\x03",

            "#057FPoint is, animals have better instincts\x01",
            "about this sorta stuff than us humans do.\x02\x03",

            "We'd better keep our eyes open for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1002FYeah...good point.\x02\x03",

            "Back to the guildhouse for us, then,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        "#050FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x80)
    OP_28(0x93, 0x1, 0x100)
    OP_28(0x93, 0x1, 0x200)
    OP_28(0x93, 0x1, 0x2000)
    Return()

    # Function_7_987 end

    def Function_8_16CA(): pass

    label("Function_8_16CA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E1")
    Call(0, 12)
    Call(0, 13)

    label("loc_16E1")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(-69550, -70, 106980, 0)
    OP_67(0, 13560, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(9000, 0)
    OP_6E(342, 0)
    SetChrPos(0x101, -43050, 40, 15070, 0)
    SetChrPos(0x106, -44190, -50, 15060, 0)
    SetChrPos(0x107, -44150, -20, 13590, 0)
    SetChrPos(0xF9, -43040, 50, 13500, 0)

    def lambda_178B():
        OP_6D(-44930, -70, 26000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_178B)

    def lambda_17A3():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A3)
    OP_C8(0x200, 0x46, "C_PLAC13._CH", 0x1, 0x7D0)
    OP_DE("Nebel Valley")
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5000)

    def lambda_17E5():
        OP_8E(0xFE, 0xFFFF58BC, 0x50, 0x602C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17E5)
    Sleep(200)

    def lambda_1805():
        OP_8E(0xFE, 0xFFFF53E4, 0x46, 0x5FFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1805)

    def lambda_1820():
        OP_8E(0xFE, 0xFFFF5510, 0xFFFFFFA6, 0x5AAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1820)
    Sleep(200)

    def lambda_1840():
        OP_8E(0xFE, 0xFFFF59CA, 0x14, 0x5B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_1840)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(-43060, 0, 25330, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x2)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1006F#4POkay, then. First we need to visit that little\x01",
            "hut on the eastern side of the valley, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        "#050F#6PYeah, let's hurry.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_A2(0x1A25)
    EventEnd(0x0)
    Return()

    # Function_8_16CA end

    def Function_9_1965(): pass

    label("Function_9_1965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1972")
    Return()

    label("loc_1972")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1989")
    Call(0, 12)
    Call(0, 13)

    label("loc_1989")

    Fade(1000)
    OP_6D(-41580, 3920, 104490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -41200, 4019, 103610, 315)
    SetChrPos(0x106, -42230, 4090, 103100, 315)
    SetChrPos(0x107, -41860, 4010, 101920, 315)
    SetChrPos(0xF9, -40840, 3940, 102310, 315)

    def lambda_1A15():

        label("loc_1A15")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1A15")

    QueueWorkItem2(0x101, 1, lambda_1A15)

    def lambda_1A26():

        label("loc_1A26")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1A26")

    QueueWorkItem2(0x106, 1, lambda_1A26)

    def lambda_1A37():

        label("loc_1A37")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1A37")

    QueueWorkItem2(0x107, 1, lambda_1A37)

    def lambda_1A48():

        label("loc_1A48")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1A48")

    QueueWorkItem2(0xF9, 1, lambda_1A48)
    OP_8C(0x9, 180, 0)
    OP_4A(0x9, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0x9,
        "#6PLooks like you made it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        "#052F#6POld-timer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1011FSo if we cross that bridge...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#6PAye, go straight across and you'll\x01",
            "reach a rocky mountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#6PIt's got a cave in it that'll let you\x01",
            "climb up farther.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#6PYour dragon's over that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1006FGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#051F#6PWe owe you, Whemler.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "#6PIf that's all for you sprouts, then,\x01",
            "I'll be heading back to my hut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "#6PMind yourselves, though, that cave's\x01",
            "packed with all manner of nastiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#6PIf things get dangerous, don't be stupid.\x01",
            "Turn around and rest up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#6PIf you need a break, come by the hut and\x01",
            "I'll help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1018FThanks, Mr. Whemler!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x106,
        "#051F#6PWe'll be careful.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF568C, 0x1018, 0x19172, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF7036, 0xF6E, 0x17016, 0x7D0, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_A2(0x1A27)
    OP_28(0x96, 0x1, 0x100)
    OP_28(0x96, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_9_1965 end

    def Function_10_1D68(): pass

    label("Function_10_1D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D75")
    Return()

    label("loc_1D75")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D8C")
    Call(0, 12)
    Call(0, 13)

    label("loc_1D8C")

    Fade(1000)
    OP_6D(-63540, 4100, 187850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(34000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -64340, 4050, 187170, 0)
    SetChrPos(0x106, -63060, 4019, 187180, 0)
    SetChrPos(0x107, -62880, 4000, 186090, 0)
    SetChrPos(0xF9, -64400, 4090, 185850, 0)
    OP_0D()

    ChrTalk(    #52
        0x101,
        "#1002F#6PSo this is where the dragon is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        "#062F#4P*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        "#051FHeh, time to really get serious.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EEC")

    ChrTalk(    #55
        0x103,
        (
            "#023F#4PWait, before we go in.\x02\x03",

            "#020FWe should probably contact the\x01",
            "Arseille first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2080")

    label("loc_1EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F7F")

    ChrTalk(    #56
        0x105,
        (
            "#044F#4PAh! Wait a moment!\x02\x03",

            "#040FWe promised we would contact Morgan aboard\x01",
            "the Arseille when we found the dragon,\x01",
            "remember?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2080")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(    #57
        0x104,
        (
            "#035F#4PWait, something occurs to me.\x02\x03",

            "#030FDid we not promise to contact the Arseille\x01",
            "once we cornered our quarry?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2080")

    label("loc_2009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2080")

    ChrTalk(    #58
        0x108,
        (
            "#073F#4PWait a moment.\x02\x03",

            "#070FWe should contact the Arseille now that\x01",
            "we've found the dragon's lair.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2080")

    TurnDirection(0x101, 0xF9, 400)

    ChrTalk(    #59
        0x101,
        "#1006F#6PRight, good point!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C8")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #60
        "\x07\x05Estelle jotted down a short description of the situation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_211B():

        label("loc_211B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_211B")

    QueueWorkItem2(0x106, 1, lambda_211B)

    def lambda_212C():

        label("loc_212C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_212C")

    QueueWorkItem2(0x107, 1, lambda_212C)

    def lambda_213D():

        label("loc_213D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_213D")

    QueueWorkItem2(0xF9, 1, lambda_213D)

    def lambda_214E():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_214E)

    def lambda_2166():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2166)
    OP_8E(0x101, 0xFFFEFE80, 0xFDB, 0x2D9BA, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_21A3():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_21A3)

    def lambda_21B1():
        OP_8C(0xF9, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_21B1)
    Sleep(300)

    ChrTalk(    #61
        0x101,
        "#1005F#6P#3SSieg!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0x197, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-68540, 5590, 186890, 1500)
    SetChrPos(0xA, -78030, 10000, 185300, 0)
    SetChrChipByIndex(0xA, 12)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    OP_43(0xA, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x1)
    Sleep(500)

    def lambda_222C():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_222C)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2249():
        OP_8E(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2249)
    Sleep(2400)
    SetChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 15)
    OP_8C(0xA, 180, 100)
    OP_8F(0xA, 0xFFFEFDD6, 0x1068, 0x2DA8C, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    OP_8C(0x101, 225, 0)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #62
        0xA,
        "#311F#6PScreee! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1016F#7PHaha. Yay, you really did follow us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x107,
        "#061FThank you, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        "#551FMan, that falcon makes no freakin' sense.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05Estelle attached her note to Sieg's leg.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #67
        0x101,
        (
            "#1006F#7POkay, then, Sieg.\x02\x03",

            "Can you take that note to the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#310F#6PScree!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0xA, -66090, 4200, 187020, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)

    def lambda_2428():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2428)
    OP_8F(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x7D0, 0x0)
    OP_8C(0xA, 270, 100)
    SetChrChipByIndex(0xA, 12)

    def lambda_2456():
        OP_6D(-68540, 5590, 186890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2456)

    def lambda_246E():
        OP_8E(0xA, 0xFFFECD84, 0x2710, 0x2D3D4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_246E)
    Sleep(100)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x80)

    def lambda_24A2():
        OP_6D(-63540, 4100, 187850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24A2)
    Sleep(1000)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x2)
    Jump("loc_292F")

    label("loc_24C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        "\x07\x05Kloe quickly wrote a description of the situation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_2526():

        label("loc_2526")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_2526")

    QueueWorkItem2(0x101, 1, lambda_2526)

    def lambda_2537():

        label("loc_2537")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_2537")

    QueueWorkItem2(0x106, 1, lambda_2537)

    def lambda_2548():

        label("loc_2548")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_2548")

    QueueWorkItem2(0x107, 1, lambda_2548)

    def lambda_2559():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2559)

    def lambda_2571():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2571)
    OP_8E(0x105, 0xFFFEFE80, 0xFDB, 0x2D9BA, 0x7D0, 0x0)

    def lambda_259D():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_259D)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)

    def lambda_25BC():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_25BC)

    def lambda_25CA():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25CA)
    Sleep(300)

    ChrTalk(    #70
        0x105,
        "#042F#6P#3SSieg, come!\x02",
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-68540, 5590, 186890, 1500)
    SetChrPos(0xA, -78030, 10000, 185300, 0)
    SetChrChipByIndex(0xA, 12)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    OP_43(0xA, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x1)
    Sleep(500)

    def lambda_2645():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2645)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2662():
        OP_8E(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2662)
    Sleep(2400)
    SetChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 15)

    def lambda_2691():
        OP_8C(0xA, 180, 100)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2691)

    def lambda_269F():
        OP_8C(0x105, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_269F)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 14)
    SetChrSubChip(0x105, 2)
    WaitChrThread(0xA, 0x3)
    OP_8F(0xA, 0xFFFEFDD6, 0x1068, 0x2DA8C, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x105, 14)
    SetChrSubChip(0x105, 0)
    OP_0D()

    ChrTalk(    #71
        0xA,
        "#311F#6PScreeee. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        "#048F#7PHaha. Hello there, you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1001FThanks, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x106,
        "#551FMan, that bird makes no freakin' sense.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x05Kloe attached her note to Sieg's leg.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #76
        0x105,
        (
            "#042F#7PAll right, Sieg. Listen closely.\x02\x03",

            "I need you to deliver that note to Morgan\x01",
            "and Julia aboard the Arseille.\x01",
            "Can you do that for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "#310F#6PScreee!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrPos(0xA, -66090, 4200, 187020, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)

    def lambda_2892():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2892)
    OP_8F(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x7D0, 0x0)
    OP_8C(0xA, 270, 100)
    SetChrChipByIndex(0xA, 12)

    def lambda_28C0():
        OP_6D(-68540, 5590, 186890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28C0)

    def lambda_28D8():
        OP_8E(0xA, 0xFFFECD84, 0x2710, 0x2D3D4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_28D8)
    Sleep(100)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x80)

    def lambda_290C():
        OP_6D(-63540, 4100, 187850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_290C)
    Sleep(1000)
    OP_8C(0x105, 90, 400)
    WaitChrThread(0x101, 0x2)

    label("loc_292F")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_296F")

    ChrTalk(    #78
        0x105,
        "#047FAll right. Now we are prepared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A4F")

    label("loc_296F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BA")

    ChrTalk(    #79
        0x103,
        "#026F#2PRight... That's preparations out of the way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A4F")

    label("loc_29BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A11")

    ChrTalk(    #80
        0x104,
        (
            "#035F#2PAnd now we are prepared to enter\x01",
            "the belly of the beast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4F")

    label("loc_2A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A4F")

    ChrTalk(    #81
        0x108,
        "#074F#2PRight. That's everything, I think.\x02",
    )

    CloseMessageWindow()

    label("loc_2A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A85")

    ChrTalk(    #82
        0x101,
        "#1002F#2POkay... Let's do this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAA")

    label("loc_2A85")


    ChrTalk(    #83
        0x101,
        "#1002F#5POkay... Let's do this!\x02",
    )

    CloseMessageWindow()

    label("loc_2AAA")


    ChrTalk(    #84
        0x107,
        "#062F#2PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#054F#4PLet's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-63660, 4000, 183220, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -63660, 4000, 183220, 0)
    SetChrPos(0x1, -63660, 4000, 183220, 0)
    SetChrPos(0x2, -63660, 4000, 183220, 0)
    SetChrPos(0x3, -63660, 4000, 183220, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x1A28)
    OP_28(0x96, 0x1, 0x400)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1D68 end

    def Function_11_2B81(): pass

    label("Function_11_2B81")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_2C37"),
        (1, "loc_2C3D"),
        (SWITCH_DEFAULT, "loc_2C43"),
    )


    label("loc_2C37")

    OP_A2(0x1200)
    Jump("loc_2C43")

    label("loc_2C3D")

    OP_A2(0x1201)
    Jump("loc_2C43")

    label("loc_2C43")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_2B81 end

    def Function_12_2C7F(): pass

    label("Function_12_2C7F")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_2CFB"),
        (1, "loc_2D01"),
        (SWITCH_DEFAULT, "loc_2D07"),
    )


    label("loc_2CFB")

    OP_A2(0x1200)
    Jump("loc_2D07")

    label("loc_2D01")

    OP_A2(0x1201)
    Jump("loc_2D07")

    label("loc_2D07")

    Return()

    # Function_12_2C7F end

    def Function_13_2D08(): pass

    label("Function_13_2D08")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_13_2D08 end

    SaveToFile()

Try(main)
