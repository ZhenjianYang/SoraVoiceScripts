from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7426   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7426.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Tildawn',                              # 9
        'Arrow Balloon',                        # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14840 ._CH',             # 00
        'ED6_DT29/CH14840 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14881 ._CH',             # 03
        'ED6_DT29/CH14040 ._CH',             # 04
        'ED6_DT29/CH14040 ._CH',             # 05
        'ED6_DT29/CH14890 ._CH',             # 06
        'ED6_DT29/CH14890 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14840P._CP',             # 00
        'ED6_DT29/CH14840P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14881P._CP',             # 03
        'ED6_DT29/CH14040P._CP',             # 04
        'ED6_DT29/CH14040P._CP',             # 05
        'ED6_DT29/CH14890P._CP',             # 06
        'ED6_DT29/CH14890P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -90260,
        Z                   = 0,
        Y                   = -73990,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -93990,
        Z                   = 0,
        Y                   = -77780,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -97810,
        Z                   = 0,
        Y                   = -73980,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94000,
        Z                   = 0,
        Y                   = -70240,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19620,
        Z                   = 6000,
        Y                   = 113250,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15450,
        Z                   = 6000,
        Y                   = 124860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -8240,
        Y                   = 5000,
        Z                   = 249100,
        Range               = 160,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x3DD1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -94060,
        TriggerZ            = 0,
        TriggerY            = -74020,
        TriggerRange        = 1000,
        ActorX              = -94060,
        ActorZ              = 1000,
        ActorY              = -74020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23590,
        TriggerZ            = 6000,
        TriggerY            = 112970,
        TriggerRange        = 1000,
        ActorX              = -23590,
        ActorZ              = 7000,
        ActorY              = 112970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19950,
        TriggerZ            = 6000,
        TriggerY            = 116710,
        TriggerRange        = 1000,
        ActorX              = -19950,
        ActorZ              = 7000,
        ActorY              = 116710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19950,
        TriggerZ            = 6000,
        TriggerY            = 109240,
        TriggerRange        = 1000,
        ActorX              = -19950,
        ActorZ              = 7000,
        ActorY              = 109240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19860,
        TriggerZ            = 6000,
        TriggerY            = 125000,
        TriggerRange        = 1000,
        ActorX              = 19860,
        ActorZ              = 7000,
        ActorY              = 125000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15980,
        TriggerZ            = 6000,
        TriggerY            = 128820,
        TriggerRange        = 1000,
        ActorX              = 15980,
        ActorZ              = 7000,
        ActorY              = 128820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16010,
        TriggerZ            = 6000,
        TriggerY            = 121230,
        TriggerRange        = 1000,
        ActorX              = 16010,
        ActorZ              = 7000,
        ActorY              = 121230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_35D",          # 01, 1
        "Function_2_47B",          # 02, 2
        "Function_3_5B5",          # 03, 3
        "Function_4_6F8",          # 04, 4
        "Function_5_841",          # 05, 5
        "Function_6_98D",          # 06, 6
        "Function_7_A21",          # 07, 7
        "Function_8_B3C",          # 08, 8
        "Function_9_C71",          # 09, 9
        "Function_10_12BB",        # 0A, 10
        "Function_11_12F8",        # 0B, 11
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 6500, 260810, 180)

    def lambda_326():

        label("loc_326")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_326")

    QueueWorkItem2(0x10, 3, lambda_326)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 8500, 260230, 180)

    def lambda_34F():

        label("loc_34F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_34F")

    QueueWorkItem2(0x11, 3, lambda_34F)

    label("loc_35C")

    Return()

    # Function_0_2FE end

    def Function_1_35D(): pass

    label("Function_1_35D")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD")
    OP_6F(0x0, 0)
    Jump("loc_3E4")

    label("loc_3DD")

    OP_6F(0x0, 60)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    OP_6F(0x1, 0)
    Jump("loc_3FD")

    label("loc_3F6")

    OP_6F(0x1, 60)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F")
    OP_6F(0x2, 0)
    Jump("loc_416")

    label("loc_40F")

    OP_6F(0x2, 60)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428")
    OP_6F(0x3, 0)
    Jump("loc_42F")

    label("loc_428")

    OP_6F(0x3, 60)

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    OP_6F(0x4, 0)
    Jump("loc_448")

    label("loc_441")

    OP_6F(0x4, 60)

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A")
    OP_6F(0x5, 0)
    Jump("loc_461")

    label("loc_45A")

    OP_6F(0x5, 60)

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473")
    OP_6F(0x6, 0)
    Jump("loc_47A")

    label("loc_473")

    OP_6F(0x6, 60)

    label("loc_47A")

    Return()

    # Function_1_35D end

    def Function_2_47B(): pass

    label("Function_2_47B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_554")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17F, 1)"), scpexpr(EXPR_END)), "loc_4E9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x7F\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCD)
    Jump("loc_551")

    label("loc_4E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x7F\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x7F\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_551")

    Jump("loc_5A7")

    label("loc_554")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I'm really proud of you for making it this far.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_5A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_47B end

    def Function_3_5B5(): pass

    label("Function_3_5B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_623")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCE)
    Jump("loc_68B")

    label("loc_623")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_68B")

    Jump("loc_6EA")

    label("loc_68E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Phew! Thanks. It was getting a little cluttered in here.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_6EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5B5 end

    def Function_4_6F8(): pass

    label("Function_4_6F8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x599, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_766")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xFB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CCF)
    Jump("loc_7CE")

    label("loc_766")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xFB\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFB\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_7CE")

    Jump("loc_833")

    label("loc_7D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05The chest is appears honored that you have taken its contents.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_833")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6F8 end

    def Function_5_841(): pass

    label("Function_5_841")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_8AF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x06\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD0)
    Jump("loc_917")

    label("loc_8AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x06\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x06\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_917")

    Jump("loc_97F")

    label("loc_91A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Thanks for playing these games. My coding fingers are going numb!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_97F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_841 end

    def Function_6_98D(): pass

    label("Function_6_98D")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CD1)
    Jump("loc_A0A")

    label("loc_9DE")


    AnonymousTalk(    #12
        "\x07\x05Keep dreaming of a wonderful future.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A0A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_6_98D end

    def Function_7_A21(): pass

    label("Function_7_A21")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_A8F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05Found \x1F\xFA\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD2)
    Jump("loc_AF7")

    label("loc_A8F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05Found \x1F\xFA\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFA\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_AF7")

    Jump("loc_B2E")

    label("loc_AFA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Everything good?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_B2E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A21 end

    def Function_8_B3C(): pass

    label("Function_8_B3C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C15")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_BAA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CD3)
    Jump("loc_C12")

    label("loc_BAA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05Found \x1F\x04\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x04\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_C12")

    Jump("loc_C63")

    label("loc_C15")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05This chest isn't empty; it's full of hope.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_C63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B3C end

    def Function_9_C71(): pass

    label("Function_9_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 3)), scpexpr(EXPR_END)), "loc_C79")
    Return()

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 4)), scpexpr(EXPR_END)), "loc_D7B")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    SetChrPos(0x0, -4780, 6000, 249400, 0)
    SetChrPos(0x1, -3370, 6000, 249200, 0)
    SetChrPos(0x2, -5020, 6000, 247450, 0)
    SetChrPos(0x3, -3250, 6000, 247430, 0)
    OP_6D(-2700, 6000, 254320, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(45000, 0)
    OP_6E(462, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)
    Jump("loc_FBB")

    label("loc_D7B")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 8500, 260810, 180)

    def lambda_DAD():

        label("loc_DAD")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_DAD")

    QueueWorkItem2(0x10, 3, lambda_DAD)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 11500, 260230, 180)

    def lambda_DE1():

        label("loc_DE1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_DE1")

    QueueWorkItem2(0x11, 3, lambda_DE1)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_E1B():
        OP_6D(-1490, 6000, 262240, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E1B)

    def lambda_E33():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E33)

    def lambda_E4B():
        OP_6B(2340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E4B)

    def lambda_E5B():
        OP_6E(454, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_E5B)

    def lambda_E6B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E6B)
    Sleep(100)

    def lambda_E7E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E7E)
    Sleep(100)

    def lambda_E91():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E91)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, -4780, 6000, 249400, 0)
    SetChrPos(0x1, -3370, 6000, 249200, 0)
    SetChrPos(0x2, -5020, 6000, 247450, 0)
    SetChrPos(0x3, -3250, 6000, 247430, 0)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_F11():
        OP_6D(-2700, 6000, 254320, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_F11)

    def lambda_F29():
        OP_67(0, 6360, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F29)

    def lambda_F41():
        OP_6B(2210, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_F41)

    def lambda_F51():
        OP_6E(465, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_F51)
    WaitChrThread(0x0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)

    label("loc_FBB")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_FCA():
        OP_6D(-2800, 6000, 251750, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_FCA)

    def lambda_FE2():
        OP_67(0, 6330, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_FE2)

    def lambda_FFA():
        OP_6B(1920, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_FFA)

    def lambda_100A():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_100A)
    SetChrChipByIndex(0x11, 3)

    def lambda_101F():
        OP_8F(0xFE, 0xFFFFF0D8, 0x1B58, 0x3CD70, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_101F)

    def lambda_103A():

        label("loc_103A")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_103A")

    QueueWorkItem2(0x11, 3, lambda_103A)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_1057():
        OP_8F(0xFE, 0xFFFFF0D8, 0x1964, 0x3CD70, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1057)

    def lambda_1072():

        label("loc_1072")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1072")

    QueueWorkItem2(0x10, 3, lambda_1072)
    WaitChrThread(0x0, 0x3)
    Battle(0x333, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_10B1"),
        (2, "loc_1182"),
        (1, "loc_12A5"),
        (SWITCH_DEFAULT, "loc_12AA"),
    )


    label("loc_10B1")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(-4240, 6000, 254970, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -4240, 6000, 254970, 0)
    SetChrPos(0x1, -4240, 6000, 254970, 0)
    SetChrPos(0x2, -4240, 6000, 254970, 0)
    SetChrPos(0x3, -4240, 6000, 254970, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C33)
    Jump("loc_12AA")

    label("loc_1182")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -4140, 6500, 260810, 180)

    def lambda_11B9():

        label("loc_11B9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_11B9")

    QueueWorkItem2(0x10, 3, lambda_11B9)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -2570, 8500, 260230, 180)

    def lambda_11E2():

        label("loc_11E2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_11E2")

    QueueWorkItem2(0x11, 3, lambda_11E2)
    OP_6D(-4280, 6000, 247440, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -4280, 6000, 247440, 0)
    SetChrPos(0x1, -4280, 6000, 247440, 0)
    SetChrPos(0x2, -4280, 6000, 247440, 0)
    SetChrPos(0x3, -4280, 6000, 247440, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C34)
    Jump("loc_12AA")

    label("loc_12A5")

    OP_B4(0x0)
    Jump("loc_12AA")

    label("loc_12AA")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_C71 end

    def Function_10_12BB(): pass

    label("Function_10_12BB")


    def lambda_12C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12C1)

    def lambda_12D3():
        OP_8F(0xFE, 0xFFFFEFD4, 0x1964, 0x3FACA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12D3)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_10_12BB end

    def Function_11_12F8(): pass

    label("Function_11_12F8")


    def lambda_12FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12FE)

    def lambda_1310():
        OP_8F(0xFE, 0xFFFFF5F6, 0x2134, 0x3F886, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1310)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_11_12F8 end

    SaveToFile()

Try(main)
