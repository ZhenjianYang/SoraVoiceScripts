from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5612   ._SN',
        MapName             = 'Other',
        Location            = 'C5612.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12320 ._CH',             # 02
        'ED6_DT29/CH12321 ._CH',             # 03
        'ED6_DT29/CH12330 ._CH',             # 04
        'ED6_DT29/CH12331 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12320P._CP',             # 02
        'ED6_DT29/CH12321P._CP',             # 03
        'ED6_DT29/CH12330P._CP',             # 04
        'ED6_DT29/CH12331P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
    )

    DeclNpc(
        X                   = 55620,
        Z                   = 9000,
        Y                   = 35600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60070,
        Z                   = 0,
        Y                   = 33920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x14D,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -22330,
        Z                   = 0,
        Y                   = 127860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13930,
        Z                   = 0,
        Y                   = -4390,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -840,
        Z                   = 0,
        Y                   = 6830,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -68950,
        Z                   = 0,
        Y                   = 155090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 97120,
        Z                   = 0,
        Y                   = 86150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 48040,
        Y                   = -1000,
        Z                   = 131420,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 36070,
        Y                   = -1000,
        Z                   = 131620,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = -69010,
        TriggerZ            = 0,
        TriggerY            = 148300,
        TriggerRange        = 1000,
        ActorX              = -69010,
        ActorZ              = 0,
        ActorY              = 148960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55620,
        TriggerZ            = 8000,
        TriggerY            = 34900,
        TriggerRange        = 1000,
        ActorX              = 55620,
        ActorZ              = 8000,
        ActorY              = 35600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1700,
        TriggerZ            = 0,
        TriggerY            = -4650,
        TriggerRange        = 1000,
        ActorX              = -1040,
        ActorZ              = 0,
        ActorY              = -4650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27290,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 1000,
        ActorX              = -27990,
        ActorZ              = 0,
        ActorY              = 9990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27290,
        TriggerZ            = 0,
        TriggerY            = 7570,
        TriggerRange        = 1000,
        ActorX              = -27950,
        ActorZ              = 0,
        ActorY              = 7570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -70540,
        TriggerZ            = 0,
        TriggerY            = 100850,
        TriggerRange        = 800,
        ActorX              = -70540,
        ActorZ              = 1100,
        ActorY              = 100850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37890,
        TriggerZ            = 0,
        TriggerY            = 131750,
        TriggerRange        = 800,
        ActorX              = 37890,
        ActorZ              = 1100,
        ActorY              = 131750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8010,
        TriggerZ            = 720,
        TriggerY            = -2040,
        TriggerRange        = 800,
        ActorX              = -8010,
        ActorZ              = 720,
        ActorY              = -2040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21970,
        TriggerZ            = 20,
        TriggerY            = -1650,
        TriggerRange        = 800,
        ActorX              = -21970,
        ActorZ              = 20,
        ActorY              = -1650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34A",          # 00, 0
        "Function_1_37C",          # 01, 1
        "Function_2_46D",          # 02, 2
        "Function_3_483",          # 03, 3
        "Function_4_5BC",          # 04, 4
        "Function_5_7DC",          # 05, 5
        "Function_6_925",          # 06, 6
        "Function_7_A83",          # 07, 7
        "Function_8_C18",          # 08, 8
        "Function_9_CBB",          # 09, 9
        "Function_10_D5E",         # 0A, 10
        "Function_11_F62",         # 0B, 11
        "Function_12_17EA",        # 0C, 12
        "Function_13_1806",        # 0D, 13
        "Function_14_1822",        # 0E, 14
        "Function_15_183E",        # 0F, 15
        "Function_16_185A",        # 10, 16
        "Function_17_2119",        # 11, 17
        "Function_18_29F3",        # 12, 18
        "Function_19_2A7C",        # 13, 19
        "Function_20_2AD9",        # 14, 20
        "Function_21_2FD7",        # 15, 21
        "Function_22_34D4",        # 16, 22
        "Function_23_34E7",        # 17, 23
    )


    def Function_0_34A(): pass

    label("Function_0_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_366"),
        (123, "loc_36D"),
        (124, "loc_374"),
        (SWITCH_DEFAULT, "loc_37B"),
    )


    label("loc_366")

    Event(0, 11)
    Jump("loc_37B")

    label("loc_36D")

    Event(0, 16)
    Jump("loc_37B")

    label("loc_374")

    Event(0, 17)
    Jump("loc_37B")

    label("loc_37B")

    Return()

    # Function_0_34A end

    def Function_1_37C(): pass

    label("Function_1_37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E")
    OP_6F(0x0, 0)
    Jump("loc_395")

    label("loc_38E")

    OP_6F(0x0, 60)

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7")
    OP_6F(0x1, 0)
    Jump("loc_3AE")

    label("loc_3A7")

    OP_6F(0x1, 60)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0")
    OP_6F(0x2, 0)
    Jump("loc_3C7")

    label("loc_3C0")

    OP_6F(0x2, 60)

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9")
    OP_6F(0x3, 0)
    Jump("loc_3E0")

    label("loc_3D9")

    OP_6F(0x3, 60)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2")
    OP_6F(0x4, 0)
    Jump("loc_3F9")

    label("loc_3F2")

    OP_6F(0x4, 60)

    label("loc_3F9")

    OP_A1(0x9, 0x12)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 0)), scpexpr(EXPR_END)), "loc_446")
    OP_64(0x5, 0x1)
    OP_10(0xE, 0x1)
    OP_71(0x8, 0x10)
    Jump("loc_44E")

    label("loc_446")

    OP_10(0x8, 0x0)
    OP_72(0x8, 0x10)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 1)), scpexpr(EXPR_END)), "loc_464")
    OP_64(0x6, 0x1)
    OP_10(0x1, 0x1)
    OP_71(0x10, 0x10)
    Jump("loc_46C")

    label("loc_464")

    OP_10(0x1, 0x0)
    OP_72(0x10, 0x10)

    label("loc_46C")

    Return()

    # Function_1_37C end

    def Function_2_46D(): pass

    label("Function_2_46D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_46D")

    label("loc_482")

    Return()

    # Function_2_46D end

    def Function_3_483(): pass

    label("Function_3_483")

    OP_EA(0x2, 0xAB, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#62ITime Sepith x50\x01",
            "#60ISpace Sepith x50\x01",
            "#61IMirage Sepith x50#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D20)
    Jump("loc_5AA")

    label("loc_52F")


    AnonymousTalk(    #1
        (
            "\x07\x05I've been looted so many times that I'm thinking of putting\x01",
            "in a request to the Bracer Guild to catch the culprits.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5AA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_483 end

    def Function_4_5BC(): pass

    label("Function_4_5BC")

    OP_EA(0x2, 0x8, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A6")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_613():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_613)

    def lambda_62E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_62E)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #2
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x423, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_681"),
        (2, "loc_693"),
        (1, "loc_6A3"),
        (SWITCH_DEFAULT, "loc_6A6"),
    )


    label("loc_681")

    OP_A2(0x1D23)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_6A6")

    label("loc_693")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6A3")

    OP_B4(0x0)
    Return()

    label("loc_6A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x298, 1)"), scpexpr(EXPR_END)), "loc_6F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "Found \x1F\x98\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D22)
    Jump("loc_754")

    label("loc_6F2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        (
            "Found \x1F\x98\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x98\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_754")

    Jump("loc_7CE")

    label("loc_757")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "\x07\x05Somewhere, deep down in the last pulsing\x01",
            "remnants of your soul, you know you're a\x01",
            "monster.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5BC end

    def Function_5_7DC(): pass

    label("Function_5_7DC")

    OP_EA(0x2, 0xAC, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x162, 1)"), scpexpr(EXPR_END)), "loc_84D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\x62\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D24)
    Jump("loc_8B1")

    label("loc_84D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\x62\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x62\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_8B1")

    Jump("loc_917")

    label("loc_8B4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05This chest is as empty as that promise you\x01",
            "made. You know which one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_917")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7DC end

    def Function_6_925(): pass

    label("Function_6_925")

    OP_EA(0x2, 0xAD, 0x1, 0x0)
    OP_EA(0x2, 0xD, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A02")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_99B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D26)
    Jump("loc_9FF")

    label("loc_99B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_9FF")

    Jump("loc_A75")

    label("loc_A02")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Nothing in here. Good. We don't want people\x01",
            "refilling these while we're not looking.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A75")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_925 end

    def Function_7_A83(): pass

    label("Function_7_A83")

    OP_EA(0x2, 0xAE, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_AF4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D27)
    Jump("loc_B58")

    label("loc_AF4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_B58")

    Jump("loc_C0A")

    label("loc_B5B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05You lift the chest over your head and shake as\x01",
            "hard as you can, but nothing comes out. Well,\x01",
            "it was an impressive display of strength, at least.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C0A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A83 end

    def Function_8_C18(): pass

    label("Function_8_C18")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C93")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x1E)
    OP_73(0x11)
    OP_64(0x5, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x1C18)
    Jump("loc_CB7")

    label("loc_C93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CB7")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_CB7")

    label("loc_CB7")

    TalkEnd(0xFF)
    Return()

    # Function_8_C18 end

    def Function_9_CBB(): pass

    label("Function_9_CBB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D36")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x10, 0)
    OP_70(0x10, 0x1E)
    OP_73(0x10)
    OP_64(0x6, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x1C19)
    Jump("loc_D5A")

    label("loc_D36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5A")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_D5A")

    label("loc_D5A")

    TalkEnd(0xFF)
    Return()

    # Function_9_CBB end

    def Function_10_D5E(): pass

    label("Function_10_D5E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_D79")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_D8A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_D9B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_D9B")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_DC7"),
        (1, "loc_DD4"),
        (3, "loc_E2C"),
        (7, "loc_EA9"),
        (SWITCH_DEFAULT, "loc_F4A"),
    )


    label("loc_DC7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F4A")

    label("loc_DD4")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",      # 0
            "[Don't Use]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E0F"),
        (1, "loc_E1C"),
        (SWITCH_DEFAULT, "loc_E29"),
    )


    label("loc_E0F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E29")

    label("loc_E1C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E29")

    label("loc_E29")

    Jump("loc_F4A")

    label("loc_E2C")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Don't Use]\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E7F"),
        (1, "loc_E8C"),
        (2, "loc_E99"),
        (SWITCH_DEFAULT, "loc_EA6"),
    )


    label("loc_E7F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA6")

    label("loc_E8C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA6")

    label("loc_E99")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EA6")

    label("loc_EA6")

    Jump("loc_F4A")

    label("loc_EA9")


    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Red Cardkey]\x01",        # 0
            "[Use Green Cardkey]\x01",      # 1
            "[Use Blue Cardkey]\x01",       # 2
            "[Don't Use]\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F13"),
        (1, "loc_F20"),
        (2, "loc_F2D"),
        (3, "loc_F3A"),
        (SWITCH_DEFAULT, "loc_F47"),
    )


    label("loc_F13")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F47")

    label("loc_F20")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F47")

    label("loc_F2D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F47")

    label("loc_F3A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F47")

    label("loc_F47")

    Jump("loc_F4A")

    label("loc_F4A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_10_D5E end

    def Function_11_F62(): pass

    label("Function_11_F62")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F79")
    Call(0, 18)
    Call(0, 19)

    label("loc_F79")

    SetChrPos(0x101, 67270, 0, 29420, 270)
    SetChrPos(0x109, 67270, 0, 28510, 270)
    SetChrPos(0xF8, 68260, 0, 28510, 270)
    SetChrPos(0xF9, 68260, 0, 29420, 270)
    OP_6D(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_109C")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1085")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_109C")

    label("loc_1085")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_109C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C3")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1101")

    label("loc_10C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EA")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1101")

    label("loc_10EA")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1101")

    Sleep(1000)
    OP_8C(0x101, 315, 400)
    OP_8C(0x109, 315, 400)
    OP_8C(0xF8, 315, 400)
    OP_8C(0xF9, 315, 400)

    def lambda_1128():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1128)

    def lambda_1140():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1140)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x101,
        (
            "#1020F#6PWhat the...?!\x01",
            "That's that thing from before!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11E1():
        OP_6D(59730, 0, 33680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11E1)

    def lambda_11F9():
        OP_67(0, 8070, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11F9)

    def lambda_1211():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1211)

    def lambda_1221():
        OP_6C(350000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1221)

    def lambda_1231():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1231)
    OP_43(0x109, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xE)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0xF)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #18
        0x109,
        (
            "#1064F#5POh, boy... That's definitely the same\x01",
            "as the one beneath the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1026F#5PWhy is it here of all places...?\x02\x03",

            "#1019FAnd far more importantly, why are\x01",
            "there TWO of them now? This is already\x01",
            "complicated enough, world, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15EE")

    ChrTalk(    #20
        0x107,
        (
            "#065F#5PI'm not sure, but, um...\x02\x03",

            "This place seems sort of like a research\x01",
            "facility, so maybe they were studying it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1015F#5PStudying it? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#561F#5PWell, um...\x02\x03",

            "Like maybe for ideas for designing\x01",
            "their own archaisms...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(    #23
        0x106,
        (
            "#057F#5PYeah, that sounds about\x01",
            "right for the society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_14B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F5")

    ChrTalk(    #24
        0x103,
        (
            "#022F#5PI see...\x01",
            "That does sound about right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_14F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1544")

    ChrTalk(    #25
        0x105,
        (
            "#042F#5PKnowing the society,\x01",
            "that does seem plausible...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1544")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1575")

    ChrTalk(    #26
        0x108,
        "#072F#5PIt seems possible.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15AC")

    ChrTalk(    #27
        0x104,
        "#032F#5PHm. A distinct possibility.\x02",
    )

    CloseMessageWindow()

    label("loc_15AC")


    ChrTalk(    #28
        0x109,
        (
            "#1068F#5PThis place is in it even deeper\x01",
            "than we thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DF")

    label("loc_15EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #29
        0x104,
        (
            "#035F#5PIt does seem that way.\x02\x03",

            "#032FIf nothing else, this place is home to\x01",
            "greater horrors than we'd imagined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DF")

    label("loc_1674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E5")

    ChrTalk(    #30
        0x108,
        (
            "#074F#5PI agree...\x02\x03",

            "#072FThis place seems more a house of\x01",
            "horrors with every step we take.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DF")

    label("loc_16E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1767")

    ChrTalk(    #31
        0x105,
        (
            "#047F#5PIt is...a little terrifying.\x02\x03",

            "#042FThis...place...is even more horrific\x01",
            "than we could have guessed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DF")

    label("loc_1767")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17DF")

    ChrTalk(    #32
        0x103,
        (
            "#026F#5PIt seems that way...\x02\x03",

            "#022FIf nothing else, this place is like\x01",
            "something out of a nightmare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DF")

    Sleep(200)
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_11_F62 end

    def Function_12_17EA(): pass

    label("Function_12_17EA")

    OP_8E(0xFE, 0xEED4, 0x14, 0x7986, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_17EA end

    def Function_13_1806(): pass

    label("Function_13_1806")

    OP_8E(0xFE, 0xE970, 0x14, 0x78FA, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_1806 end

    def Function_14_1822(): pass

    label("Function_14_1822")

    OP_8E(0xFE, 0xE8E4, 0x14, 0x7454, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_1822 end

    def Function_15_183E(): pass

    label("Function_15_183E")

    OP_8E(0xFE, 0xEE8E, 0x14, 0x7472, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_183E end

    def Function_16_185A(): pass

    label("Function_16_185A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1871")
    Call(0, 18)
    Call(0, 19)

    label("loc_1871")

    SetChrPos(0x101, 60570, 4000, 21850, 0)
    SetChrPos(0x109, 59450, 4000, 21810, 0)
    SetChrPos(0xF8, 59430, 4000, 20670, 0)
    SetChrPos(0xF9, 60900, 4000, 20660, 0)
    OP_6D(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1956")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1994")

    label("loc_1956")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197D")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1994")

    label("loc_197D")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BB")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19F9")

    label("loc_19BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19F9")

    label("loc_19E2")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19F9")

    Sleep(1000)

    def lambda_1A04():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A04)

    def lambda_1A1C():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A1C)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #33
        0x101,
        (
            "#1020F#6PWhat the...?!\x01",
            "That's that thing from before!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ABD():
        OP_6D(59950, 4000, 27700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ABD)

    def lambda_1AD5():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1AD5)

    def lambda_1AE5():
        OP_6E(283, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AE5)

    def lambda_1AF5():
        OP_67(0, 7140, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1AF5)

    def lambda_1B0D():
        OP_8E(0xFE, 0xEC0E, 0xFA0, 0x5B72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B0D)
    Sleep(50)

    def lambda_1B2D():
        OP_8E(0xFE, 0xE8DA, 0xFA0, 0x5B72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B2D)
    Sleep(100)

    def lambda_1B4D():
        OP_8E(0xFE, 0xE5B0, 0xFA0, 0x583E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1B4D)
    Sleep(60)

    def lambda_1B6D():
        OP_8E(0xFE, 0xF0DC, 0xFA0, 0x578A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1B6D)
    WaitChrThread(0xF8, 0x1)
    OP_8C(0xF8, 0, 400)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #34
        0x109,
        (
            "#1064F#5POh, boy... That's definitely the same\x01",
            "as the one beneath the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1026F#5PWhy is it here of all places...?\x02\x03",

            "#1019FAnd far more importantly, why are\x01",
            "there TWO of them now? This is already\x01",
            "complicated enough, world, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1D")

    ChrTalk(    #36
        0x107,
        (
            "#065F#5PI'm not sure, but, um...\x02\x03",

            "This place seems sort of like a research\x01",
            "facility, so maybe they were studying it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1015F#5PStudying it? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        (
            "#561F#5PWell, um...\x02\x03",

            "Like maybe for ideas for designing\x01",
            "their own archaisms...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE0")

    ChrTalk(    #39
        0x106,
        (
            "#057F#5PYeah, that sounds about\x01",
            "right for the society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E24")

    ChrTalk(    #40
        0x103,
        (
            "#022F#5PI see...\x01",
            "That does sound about right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1E24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E73")

    ChrTalk(    #41
        0x105,
        (
            "#042F#5PKnowing the society,\x01",
            "that does seem plausible...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1E73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA4")

    ChrTalk(    #42
        0x108,
        "#072F#5PIt seems possible.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1EA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDB")

    ChrTalk(    #43
        0x104,
        "#032F#5PHm. A distinct possibility.\x02",
    )

    CloseMessageWindow()

    label("loc_1EDB")


    ChrTalk(    #44
        0x109,
        (
            "#1068F#5PThis place is in it even deeper\x01",
            "than we thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210E")

    label("loc_1F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA3")

    ChrTalk(    #45
        0x104,
        (
            "#035F#5PIt does seem that way.\x02\x03",

            "#032FIf nothing else, this place is home to\x01",
            "greater horrors than we'd imagined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210E")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2014")

    ChrTalk(    #46
        0x108,
        (
            "#074F#5PI agree...\x02\x03",

            "#072FThis place seems more a house of\x01",
            "horrors with every step we take.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210E")

    label("loc_2014")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2096")

    ChrTalk(    #47
        0x105,
        (
            "#047F#5PIt is...a little terrifying.\x02\x03",

            "#042FThis...place...is even more horrific\x01",
            "than we could have guessed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210E")

    label("loc_2096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210E")

    ChrTalk(    #48
        0x103,
        (
            "#026F#5PIt seems that way...\x02\x03",

            "#022FIf nothing else, this place is like\x01",
            "something out of a nightmare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210E")

    Sleep(200)
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_16_185A end

    def Function_17_2119(): pass

    label("Function_17_2119")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2130")
    Call(0, 18)
    Call(0, 19)

    label("loc_2130")

    SetChrPos(0x101, 52920, 8000, 28620, 90)
    SetChrPos(0x109, 52800, 8000, 29590, 90)
    SetChrPos(0xF8, 51980, 8000, 28450, 90)
    SetChrPos(0xF9, 51750, 8000, 29450, 90)
    OP_6D(52120, 8000, 28960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #49
        0x101,
        "#1004F#6PHuh? A balcony of some sort...\x02",
    )

    CloseMessageWindow()
    OP_8F(0x101, 0xD46C, 0x1F40, 0x72D8, 0x7D0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_221E():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221E)

    def lambda_2236():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2236)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(52850, 8000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #50
        0x101,
        (
            "#1020F#6PWhat the...?!\x01",
            "That's that thing from before!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22D7():
        OP_6D(60080, 8000, 30590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22D7)

    def lambda_22EF():
        OP_67(0, 8189, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_22EF)

    def lambda_2307():
        OP_6C(297000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2307)

    def lambda_2317():
        OP_6E(363, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2317)

    def lambda_2327():
        OP_6B(2710, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_2327)

    def lambda_2337():
        OP_8E(0xFE, 0xD444, 0x1F40, 0x75F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2337)
    Sleep(50)

    def lambda_2357():
        OP_8E(0xFE, 0xD426, 0x1F40, 0x790E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2357)
    Sleep(50)

    def lambda_2377():
        OP_8E(0xFE, 0xD46C, 0x1F40, 0x6F86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2377)
    WaitChrThread(0x109, 0x1)

    def lambda_2397():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2397)
    WaitChrThread(0xF8, 0x1)

    def lambda_23AA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_23AA)
    WaitChrThread(0xF9, 0x1)

    def lambda_23BD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_23BD)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #51
        0x109,
        (
            "#1064F#6PIt's a bit hard to see from here, but...\x02\x03",

            "Yeah, that...does look like the one\x01",
            "beneath the castle, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1026F#6PWhy is it here of all places...?\x02\x03",

            "#1019FAnd far more importantly, why are\x01",
            "there TWO of them now? This is already\x01",
            "complicated enough, world, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2770")

    ChrTalk(    #53
        0x107,
        (
            "#065F#6PI'm not sure, but, um...\x02\x03",

            "This place seems sort of like a research\x01",
            "facility, so maybe they were studying it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1015F#6PStudying it? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        (
            "#561F#6PWell, um...\x02\x03",

            "Like maybe for ideas for designing\x01",
            "their own archaisms...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2633")

    ChrTalk(    #56
        0x106,
        (
            "#057F#6PYeah, that sounds about\x01",
            "right for the society.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_2633")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2677")

    ChrTalk(    #57
        0x103,
        (
            "#022F#6PI see...\x01",
            "That does sound about right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_2677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C6")

    ChrTalk(    #58
        0x105,
        (
            "#042F#6PKnowing the society,\x01",
            "that does seem plausible...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_26C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F7")

    ChrTalk(    #59
        0x108,
        "#072F#6PIt seems possible.\x02",
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_26F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_272E")

    ChrTalk(    #60
        0x104,
        "#032F#6PHm. A distinct possibility.\x02",
    )

    CloseMessageWindow()

    label("loc_272E")


    ChrTalk(    #61
        0x109,
        (
            "#1068F#6PThis place is in it even deeper\x01",
            "than we thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2961")

    label("loc_2770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27F6")

    ChrTalk(    #62
        0x104,
        (
            "#035F#6PIt does seem that way.\x02\x03",

            "#032FIf nothing else, this place is home to\x01",
            "greater horrors than we'd imagined.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2961")

    label("loc_27F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2867")

    ChrTalk(    #63
        0x108,
        (
            "#074F#6PI agree...\x02\x03",

            "#072FThis place seems more a house of\x01",
            "horrors with every step we take.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2961")

    label("loc_2867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E9")

    ChrTalk(    #64
        0x105,
        (
            "#047F#6PIt is...a little terrifying.\x02\x03",

            "#042FThis...place...is even more horrific\x01",
            "than we could have guessed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2961")

    label("loc_28E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2961")

    ChrTalk(    #65
        0x103,
        (
            "#026F#6PIt seems that way...\x02\x03",

            "#022FIf nothing else, this place is like\x01",
            "something out of a nightmare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2961")

    Sleep(200)
    Fade(500)
    OP_6D(54380, 8000, 29400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 54380, 8000, 29400, 90)
    SetChrPos(0x1, 54380, 8000, 29400, 90)
    SetChrPos(0x2, 54380, 8000, 29400, 90)
    SetChrPos(0x3, 54380, 8000, 29400, 90)
    OP_0D()
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_17_2119 end

    def Function_18_29F3(): pass

    label("Function_18_29F3")

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
        (0, "loc_2A6F"),
        (1, "loc_2A75"),
        (SWITCH_DEFAULT, "loc_2A7B"),
    )


    label("loc_2A6F")

    OP_A2(0x1200)
    Jump("loc_2A7B")

    label("loc_2A75")

    OP_A2(0x1201)
    Jump("loc_2A7B")

    label("loc_2A7B")

    Return()

    # Function_18_29F3 end

    def Function_19_2A7C(): pass

    label("Function_19_2A7C")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_19_2A7C end

    def Function_20_2AD9(): pass

    label("Function_20_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D4F")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1004FThat's a Gospel, isn't it?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -7520, 20, -3140, 0)
    SetChrPos(0x1, -8620, 20, -3320, 0)
    SetChrPos(0x2, -9230, 20, -4070, 0)
    SetChrPos(0x3, -6590, 20, -3840, 0)

    def lambda_2BB4():
        OP_6D(-8010, 730, -510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BB4)

    def lambda_2BCC():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BCC)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C15")

    ChrTalk(    #68
        0x105,
        "#042FIt seems to be, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDE")

    label("loc_2C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C47")

    ChrTalk(    #69
        0x104,
        "#032FIt appears to be, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDE")

    label("loc_2C47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C77")

    ChrTalk(    #70
        0x106,
        "#050FSure looks like one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDE")

    label("loc_2C77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA9")

    ChrTalk(    #71
        0x107,
        "#062FUh-huh, I think it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDE")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CDE")

    ChrTalk(    #72
        0x108,
        "#072FIt looks like one, at least.\x02",
    )

    CloseMessageWindow()

    label("loc_2CDE")


    ChrTalk(    #73
        0x101,
        (
            "#1015FDoesn't look like we can\x01",
            "do anything with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1063FMust be part of their experiments.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C90)
    EventEnd(0x0)
    Jump("loc_2FD6")

    label("loc_2D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9D")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #75
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8C(0x0, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        "#1004FThat's a Gospel, isn't it?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -7520, 20, -3140, 0)
    SetChrPos(0x1, -8620, 20, -3320, 0)
    SetChrPos(0x2, -9230, 20, -4070, 0)
    SetChrPos(0x3, -6590, 20, -3840, 0)

    def lambda_2E30():
        OP_6D(-8010, 730, -510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E30)

    def lambda_2E48():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E48)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E91")

    ChrTalk(    #77
        0x105,
        "#042FIt seems to be, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F5A")

    label("loc_2E91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EC3")

    ChrTalk(    #78
        0x104,
        "#032FIt appears to be, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F5A")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF3")

    ChrTalk(    #79
        0x106,
        "#050FSure looks like one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F5A")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F25")

    ChrTalk(    #80
        0x107,
        "#062FUh-huh, I think it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F5A")

    label("loc_2F25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5A")

    ChrTalk(    #81
        0x108,
        "#072FIt looks like one, at least.\x02",
    )

    CloseMessageWindow()

    label("loc_2F5A")


    ChrTalk(    #82
        0x101,
        (
            "#1015FDoesn't look like we can\x01",
            "do anything with it...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C90)
    EventEnd(0x0)
    Jump("loc_2FD6")

    label("loc_2F9D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_2FD6")

    Return()

    # Function_20_2AD9 end

    def Function_21_2FD7(): pass

    label("Function_21_2FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3250")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #84
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x101,
        "#1004FThat's a Gospel, isn't it?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -21420, 20, -3140, 0)
    SetChrPos(0x1, -22470, 20, -3320, 0)
    SetChrPos(0x2, -23030, 20, -4070, 0)
    SetChrPos(0x3, -20590, 20, -3840, 0)

    def lambda_30B2():
        OP_6D(-21890, 1010, -480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B2)

    def lambda_30CA():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30CA)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_311B")

    ChrTalk(    #86
        0x108,
        "#072FIt looks like one, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DF")

    label("loc_311B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_314D")

    ChrTalk(    #87
        0x107,
        "#062FUh-huh, I think it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DF")

    label("loc_314D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3180")

    ChrTalk(    #88
        0x103,
        "#022FQuite a large one, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DF")

    label("loc_3180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B0")

    ChrTalk(    #89
        0x106,
        "#050FSure looks like one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DF")

    label("loc_31B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DF")

    ChrTalk(    #90
        0x104,
        "#032FIt appears to be, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_31DF")


    ChrTalk(    #91
        0x101,
        (
            "#1015FDoesn't look like we can\x01",
            "do anything with it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        "#1063FMust be part of their experiments.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C91)
    EventEnd(0x0)
    Jump("loc_34D3")

    label("loc_3250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_349A")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #93
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004FThat's a Gospel, isn't it?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -21420, 20, -3140, 0)
    SetChrPos(0x1, -22470, 20, -3320, 0)
    SetChrPos(0x2, -23030, 20, -4070, 0)
    SetChrPos(0x3, -20590, 20, -3840, 0)

    def lambda_332A():
        OP_6D(-21890, 1010, -480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_332A)

    def lambda_3342():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3342)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3393")

    ChrTalk(    #95
        0x108,
        "#072FIt looks like one, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3457")

    label("loc_3393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C5")

    ChrTalk(    #96
        0x107,
        "#062FUh-huh, I think it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3457")

    label("loc_33C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F8")

    ChrTalk(    #97
        0x103,
        "#022FQuite a large one, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3457")

    label("loc_33F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3428")

    ChrTalk(    #98
        0x106,
        "#050FSure looks like one.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3457")

    label("loc_3428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3457")

    ChrTalk(    #99
        0x104,
        "#032FIt appears to be, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_3457")


    ChrTalk(    #100
        0x101,
        (
            "#1015FDoesn't look like we can\x01",
            "do anything with it...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C91)
    EventEnd(0x0)
    Jump("loc_34D3")

    label("loc_349A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05A large Gospel sits here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_34D3")

    Return()

    # Function_21_2FD7 end

    def Function_22_34D4(): pass

    label("Function_22_34D4")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A2(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_22_34D4 end

    def Function_23_34E7(): pass

    label("Function_23_34E7")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A2(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_23_34E7 end

    SaveToFile()

Try(main)
