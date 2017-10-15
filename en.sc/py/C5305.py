from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5305   ._SN',
        MapName             = 'Other',
        Location            = 'C5305.x',
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
        'エレベータ',                           # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12010 ._CH',             # 00
        'ED6_DT29/CH12010 ._CH',             # 01
        'ED6_DT29/CH12080 ._CH',             # 02
        'ED6_DT29/CH12081 ._CH',             # 03
        'ED6_DT29/CH12050 ._CH',             # 04
        'ED6_DT29/CH12051 ._CH',             # 05
        'ED6_DT29/CH12140 ._CH',             # 06
        'ED6_DT29/CH12141 ._CH',             # 07
        'ED6_DT29/CH12420 ._CH',             # 08
        'ED6_DT29/CH12421 ._CH',             # 09
        'ED6_DT29/CH12290 ._CH',             # 0A
        'ED6_DT29/CH12291 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12010P._CP',             # 00
        'ED6_DT29/CH12010P._CP',             # 01
        'ED6_DT29/CH12080P._CP',             # 02
        'ED6_DT29/CH12081P._CP',             # 03
        'ED6_DT29/CH12050P._CP',             # 04
        'ED6_DT29/CH12051P._CP',             # 05
        'ED6_DT29/CH12140P._CP',             # 06
        'ED6_DT29/CH12141P._CP',             # 07
        'ED6_DT29/CH12420P._CP',             # 08
        'ED6_DT29/CH12421P._CP',             # 09
        'ED6_DT29/CH12290P._CP',             # 0A
        'ED6_DT29/CH12291P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 60,
        Z                   = 3500,
        Y                   = -94030,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -91910,
        Z                   = 2230,
        Y                   = 96640,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -98860,
        Z                   = 50,
        Y                   = 8530,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x528,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -79920,
        Z                   = 2350,
        Y                   = -72810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83880,
        Z                   = 2180,
        Y                   = -85080,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100050,
        Y                   = -2000,
        Z                   = 9110,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -107300,
        TriggerZ            = 0,
        TriggerY            = 4900,
        TriggerRange        = 1000,
        ActorX              = -107910,
        ActorZ              = 0,
        ActorY              = 4870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107300,
        TriggerZ            = 0,
        TriggerY            = 9030,
        TriggerRange        = 1000,
        ActorX              = -107910,
        ActorZ              = 0,
        ActorY              = 9000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -107290,
        TriggerZ            = 0,
        TriggerY            = 13070,
        TriggerRange        = 1000,
        ActorX              = -107980,
        ActorZ              = 0,
        ActorY              = 12940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90700,
        TriggerZ            = 0,
        TriggerY            = 13010,
        TriggerRange        = 1000,
        ActorX              = -90050,
        ActorZ              = 0,
        ActorY              = 13040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90710,
        TriggerZ            = 0,
        TriggerY            = 8940,
        TriggerRange        = 1000,
        ActorX              = -90060,
        ActorZ              = 0,
        ActorY              = 8980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -90710,
        TriggerZ            = 0,
        TriggerY            = 5000,
        TriggerRange        = 1000,
        ActorX              = -90020,
        ActorZ              = 0,
        ActorY              = 5030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 2000,
        TriggerY            = -94060,
        TriggerRange        = 1000,
        ActorX              = 60,
        ActorZ              = 2000,
        ActorY              = -94030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_352",          # 01, 1
        "Function_2_4A9",          # 02, 2
        "Function_3_4BF",          # 03, 3
        "Function_4_61D",          # 04, 4
        "Function_5_73A",          # 05, 5
        "Function_6_8B8",          # 06, 6
        "Function_7_9F3",          # 07, 7
        "Function_8_B46",          # 08, 8
        "Function_9_C9E",          # 09, 9
        "Function_10_ED5",         # 0A, 10
        "Function_11_FFE",         # 0B, 11
        "Function_12_11ED",        # 0C, 12
        "Function_13_1439",        # 0D, 13
        "Function_14_1535",        # 0E, 14
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E7")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_30A")

    label("loc_2E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA")
    Event(0, 12)
    Jump("loc_30A")

    label("loc_2FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Event(0, 14)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_A2(0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_351")

    Return()

    # Function_0_2D6 end

    def Function_1_352(): pass

    label("Function_1_352")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0x3, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0x3, 60)

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0x4, 0)
    Jump("loc_3A5")

    label("loc_39E")

    OP_6F(0x4, 60)

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7")
    OP_6F(0x5, 0)
    Jump("loc_3BE")

    label("loc_3B7")

    OP_6F(0x5, 60)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    OP_6F(0x6, 0)
    Jump("loc_3D7")

    label("loc_3D0")

    OP_6F(0x6, 60)

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    OP_6F(0x7, 0)
    Jump("loc_3F0")

    label("loc_3E9")

    OP_6F(0x7, 60)

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402")
    OP_6F(0x8, 0)
    Jump("loc_409")

    label("loc_402")

    OP_6F(0x8, 60)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B")
    OP_6F(0x9, 0)
    Jump("loc_422")

    label("loc_41B")

    OP_6F(0x9, 60)

    label("loc_422")

    OP_10(0xE, 0x0)
    OP_71(0x1, 0x4)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_10(0x10, 0x0)
    OP_82(0x83, 0x0)
    Jump("loc_4A3")

    label("loc_452")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 600)
    OP_10(0x10, 0x1)
    OP_82(0x83, 0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1B(0x10, 0x0, 0xD)

    label("loc_4A3")

    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_352 end

    def Function_2_4A9(): pass

    label("Function_2_4A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4A9")

    label("loc_4BE")

    Return()

    # Function_2_4A9 end

    def Function_3_4BF(): pass

    label("Function_3_4BF")

    OP_EA(0x2, 0x42, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_530")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2383)
    Jump("loc_594")

    label("loc_530")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_594")

    Jump("loc_60F")

    label("loc_597")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05As you approach, the chest bursts open on its\x01",
            "own! Unfortunately, there's nothing inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_60F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4BF end

    def Function_4_61D(): pass

    label("Function_4_61D")

    OP_EA(0x2, 0x43, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_68E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2384)
    Jump("loc_6F2")

    label("loc_68E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_6F2")

    Jump("loc_72C")

    label("loc_6F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05E to the M to the P-T-Y.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_72C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_61D end

    def Function_5_73A(): pass

    label("Function_5_73A")

    OP_EA(0x2, 0x44, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_7AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2385)
    Jump("loc_80F")

    label("loc_7AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_80F")

    Jump("loc_8AA")

    label("loc_812")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You imagine this chest as it once was,\x01",
            "brimming with treasure and full of delight.\x01",
            "You can hardly bear to look at it now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_73A end

    def Function_6_8B8(): pass

    label("Function_6_8B8")

    OP_EA(0x2, 0x45, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_990")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_929")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2386)
    Jump("loc_98D")

    label("loc_929")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_98D")

    Jump("loc_9E5")

    label("loc_990")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05This treasure chest is on strike until further\x01",
            "notice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9E5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8B8 end

    def Function_7_9F3(): pass

    label("Function_7_9F3")

    OP_EA(0x2, 0x46, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x470, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_A64")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2387)
    Jump("loc_AC8")

    label("loc_A64")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_AC8")

    Jump("loc_B38")

    label("loc_ACB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05I waited four years for this game and all I got\x01",
            "was this stupid chest message.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B38")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9F3 end

    def Function_8_B46(): pass

    label("Function_8_B46")

    OP_EA(0x2, 0x47, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_BB7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2388)
    Jump("loc_C1B")

    label("loc_BB7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\x01\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x01\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_C1B")

    Jump("loc_C90")

    label("loc_C1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05There's nothing in this chest, but you imagine all\x01",
            "the things that COULD'VE been...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C90")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B46 end

    def Function_9_C9E(): pass

    label("Function_9_C9E")

    OP_EA(0x2, 0x48, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E39")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_91(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CF5():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CF5)

    def lambda_D10():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D10)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(    #18
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D63"),
        (2, "loc_D75"),
        (1, "loc_D85"),
        (SWITCH_DEFAULT, "loc_D88"),
    )


    label("loc_D63")

    OP_A2(0x238A)
    OP_6F(0x9, 60)
    Sleep(500)
    Jump("loc_D88")

    label("loc_D75")

    OP_6F(0x9, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D85")

    OP_B4(0x0)
    Return()

    label("loc_D88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x108, 1)"), scpexpr(EXPR_END)), "loc_DD4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #19
        "Found \x1F\x08\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2389)
    Jump("loc_E36")

    label("loc_DD4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #20
        (
            "Found \x1F\x08\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x08\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_E36")

    Jump("loc_EC7")

    label("loc_E39")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        (
            "\x07\x05As you look into the woodgrain of the empty\x01",
            "chest, you wonder how many chests could be\x01",
            "made out of a single tree.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EC7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C9E end

    def Function_10_ED5(): pass

    label("Function_10_ED5")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-28890, 80, 108700, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(301000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)
    Sleep(1500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x0)

    def lambda_F5D():
        OP_6D(-890, 1090, 98940, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5D)

    def lambda_F75():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F75)
    OP_6C(315000, 5000)
    OP_6B(3500, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_ED5 end

    def Function_11_FFE(): pass

    label("Function_11_FFE")

    EventBegin(0x0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 100050, -1750, 9110, 0)
    OP_48()
    Fade(1000)
    OP_6D(100050, 0, 9110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_10AE():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10AE)
    Sleep(500)

    def lambda_10CE():
        OP_6D(100050, 35000, 9110, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CE)

    def lambda_10E6():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10E6)

    def lambda_10FE():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10FE)
    Sleep(500)

    def lambda_1113():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1113)
    Sleep(500)

    def lambda_1133():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1133)
    Sleep(400)

    def lambda_1153():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1153)
    Sleep(200)

    def lambda_1173():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1173)
    Sleep(100)

    def lambda_1193():
        OP_8F(0xFE, 0x186D2, 0xFDE8, 0x2396, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1193)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A2(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_FFE end

    def Function_12_11ED(): pass

    label("Function_12_11ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 100050, 66000, 9110, 0)
    OP_48()
    OP_6D(100050, 48000, 9110, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 67000, 10000, 0)
    OP_89(0x1, 101000, 67000, 9000, 90)
    OP_89(0x2, 99000, 67000, 9000, 270)
    OP_89(0x3, 100000, 67000, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_129C():
        OP_6D(100050, 0, 9110, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_129C)

    def lambda_12B4():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12B4)

    def lambda_12CC():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_12CC)
    FadeToBright(1000, 0)
    SetPlaceName(0x11F)

    def lambda_12E8():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12E8)
    Sleep(7800)

    def lambda_1308():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1308)
    Sleep(700)

    def lambda_1328():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1328)
    Sleep(600)

    def lambda_1348():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1348)
    Sleep(100)

    def lambda_1368():
        OP_8F(0xFE, 0x186D2, 0xFFFFF92A, 0x2396, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1368)
    Sleep(500)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 99940, 0, 4350, 180)
    SetChrPos(0x1, 99940, 0, 4350, 180)
    SetChrPos(0x2, 99940, 0, 4350, 180)
    SetChrPos(0x3, 99940, 0, 4350, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_12_11ED end

    def Function_13_1439(): pass

    label("Function_13_1439")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x101, -500, 1050, 98500, 180)
    SetChrPos(0x102, -1500, 1050, 98500, 180)
    SetChrPos(0xF8, -500, 1050, 99500, 180)
    SetChrPos(0xF9, -1500, 1050, 99500, 180)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_14E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_14E4)

    def lambda_14F6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_14F6)

    def lambda_1508():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1508)

    def lambda_151A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_151A)
    Sleep(2000)
    NewScene("ED6_DT21/C5300   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1439 end

    def Function_14_1535(): pass

    label("Function_14_1535")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x101, -1500, 1050, 99500, 0)
    SetChrPos(0x102, -500, 1050, 99500, 0)
    SetChrPos(0xF8, -1500, 1050, 98500, 0)
    SetChrPos(0xF9, -500, 1050, 98500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1610():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1610)

    def lambda_1622():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1622)

    def lambda_1634():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1634)

    def lambda_1646():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1646)
    Sleep(2500)
    Fade(500)
    OP_6D(-1000, 0, 103000, 0)
    SetChrPos(0x0, -1000, 0, 103000, 0)
    SetChrPos(0x1, -1000, 0, 103000, 0)
    SetChrPos(0x2, -1000, 0, 103000, 0)
    SetChrPos(0x3, -1000, 0, 103000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_1535 end

    SaveToFile()

Try(main)
