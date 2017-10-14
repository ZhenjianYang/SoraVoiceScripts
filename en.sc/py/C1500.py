from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1500   ._SN',
        MapName             = 'Bose',
        Location            = 'C1500.x',
        MapIndex            = 61,
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
        '',                                     # 10
        'Krone Pass',                           # 11
        'West Bose Hwy',                        # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT09/CH10880 ._CH',             # 00
        'ED6_DT09/CH10881 ._CH',             # 01
        'ED6_DT09/CH11160 ._CH',             # 02
        'ED6_DT09/CH11161 ._CH',             # 03
        'ED6_DT09/CH10200 ._CH',             # 04
        'ED6_DT09/CH10201 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12440 ._CH',             # 08
        'ED6_DT29/CH12441 ._CH',             # 09
        'ED6_DT29/CH12500 ._CH',             # 0A
        'ED6_DT29/CH13030 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10880P._CP',             # 00
        'ED6_DT09/CH10881P._CP',             # 01
        'ED6_DT09/CH11160P._CP',             # 02
        'ED6_DT09/CH11161P._CP',             # 03
        'ED6_DT09/CH10200P._CP',             # 04
        'ED6_DT09/CH10201P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12440P._CP',             # 08
        'ED6_DT29/CH12441P._CP',             # 09
        'ED6_DT29/CH12500P._CP',             # 0A
        'ED6_DT29/CH13030P._CP',             # 0B
    )

    DeclNpc(
        X                   = -134573,
        Z                   = 3995,
        Y                   = 87240,
        Direction           = 315,
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
        X                   = -148670,
        Z                   = 4059,
        Y                   = 108220,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -140810,
        Z                   = 6010,
        Y                   = -31010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -119390,
        Z                   = -60,
        Y                   = 180920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -146390,
        Z                   = 2009,
        Y                   = 152190,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -148000,
        Z                   = 2090,
        Y                   = 136280,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154200,
        Z                   = 1990,
        Y                   = 120790,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154710,
        Z                   = 4070,
        Y                   = 99880,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -154180,
        Z                   = 4030,
        Y                   = 76310,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162330,
        Z                   = 4019,
        Y                   = 46020,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -131150,
        Z                   = 2040,
        Y                   = 55190,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151910,
        Z                   = 5910,
        Y                   = -11960,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -151260,
        Z                   = 4040,
        Y                   = 20370,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xCD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -134573,
        Y                   = 3500,
        Z                   = 87240,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -157500,
        Y                   = 3000,
        Z                   = 105200,
        Range               = -142800,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x1B134,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    DeclActor(
        TriggerX            = -158410,
        TriggerZ            = 1970,
        TriggerY            = 120220,
        TriggerRange        = 1000,
        ActorX              = -158970,
        ActorZ              = 1970,
        ActorY              = 120040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -124550,
        TriggerZ            = 4019,
        TriggerY            = 90450,
        TriggerRange        = 1000,
        ActorX              = -123890,
        ActorZ              = 4019,
        ActorY              = 90020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -156400,
        TriggerZ            = 3930,
        TriggerY            = 80510,
        TriggerRange        = 1000,
        ActorX              = -156750,
        ActorZ              = 3930,
        ActorY              = 81120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -170750,
        TriggerZ            = 5900,
        TriggerY            = 3230,
        TriggerRange        = 1000,
        ActorX              = -171430,
        ActorZ              = 5900,
        ActorY              = 3350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -130810,
        TriggerZ            = 4050,
        TriggerY            = 21300,
        TriggerRange        = 1000,
        ActorX              = -130139,
        ActorZ              = 4050,
        ActorY              = 21690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_37B",          # 01, 1
        "Function_2_475",          # 02, 2
        "Function_3_48B",          # 03, 3
        "Function_4_5EA",          # 04, 4
        "Function_5_75D",          # 05, 5
        "Function_6_8D7",          # 06, 6
        "Function_7_A1E",          # 07, 7
        "Function_8_AD0",          # 08, 8
        "Function_9_E13",          # 09, 9
        "Function_10_1151",        # 0A, 10
        "Function_11_1E96",        # 0B, 11
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Return()

    # Function_0_37A end

    def Function_1_37B(): pass

    label("Function_1_37B")

    OP_16(0x2, 0xFA0, 0xFFFBED08, 0xFFFF2540, 0x23003E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F")
    OP_6F(0x0, 0)
    Jump("loc_3A6")

    label("loc_39F")

    OP_6F(0x0, 60)

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8")
    OP_6F(0x1, 0)
    Jump("loc_3BF")

    label("loc_3B8")

    OP_6F(0x1, 60)

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")
    OP_6F(0x2, 0)
    Jump("loc_3D8")

    label("loc_3D1")

    OP_6F(0x2, 60)

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA")
    OP_6F(0x3, 0)
    Jump("loc_3F1")

    label("loc_3EA")

    OP_6F(0x3, 60)

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403")
    OP_6F(0x4, 0)
    Jump("loc_40A")

    label("loc_403")

    OP_6F(0x4, 60)

    label("loc_40A")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    OP_8C(0x9, 180, 0)

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    ClearChrFlags(0x9, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_467")

    Jump("loc_474")

    label("loc_46A")

    SetChrFlags(0x9, 0x80)
    OP_B2(0x0, 0x1, 0x80)

    label("loc_474")

    Return()

    # Function_1_37B end

    def Function_2_475(): pass

    label("Function_2_475")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_475")

    label("loc_48A")

    Return()

    # Function_2_475 end

    def Function_3_48B(): pass

    label("Function_3_48B")

    OP_EA(0x2, 0x55, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_4FC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B70)
    Jump("loc_560")

    label("loc_4FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_560")

    Jump("loc_5DC")

    label("loc_563")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Somewhere, deep down in the last pulsing\x01",
            "remnants of your soul, you know you're a\x01",
            "monster.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_48B end

    def Function_4_5EA(): pass

    label("Function_4_5EA")

    OP_EA(0x2, 0x56, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_65B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B71)
    Jump("loc_6BF")

    label("loc_65B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6BF")

    Jump("loc_74F")

    label("loc_6C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Oh, sure. Just take it! My name's Erik, by the\x01",
            "way. I bet asking my name never even crossed\x01",
            "your mind, did it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_74F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5EA end

    def Function_5_75D(): pass

    label("Function_5_75D")

    OP_EA(0x2, 0x57, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_835")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_7CE")
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
    OP_A2(0x1B72)
    Jump("loc_832")

    label("loc_7CE")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_832")

    Jump("loc_8C9")

    label("loc_835")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You know the chest is empty, but it has\x01",
            "served you well. Instead of opening it, you give\x01",
            "it a gentle pat on the head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8C9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_75D end

    def Function_6_8D7(): pass

    label("Function_6_8D7")

    OP_EA(0x2, 0x58, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_948")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B73)
    Jump("loc_9AC")

    label("loc_948")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_9AC")

    Jump("loc_A10")

    label("loc_9AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05There's nothing in this chest, but sometimes it's\x01",
            "good to pretend.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A10")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8D7 end

    def Function_7_A1E(): pass

    label("Function_7_A1E")

    OP_EA(0x2, 0x59, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A99")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    AddSepith(0x0, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "Found #2C#56IEarth Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B74)
    Jump("loc_ABE")

    label("loc_A99")


    AnonymousTalk(    #13
        "\x07\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_ABE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A1E end

    def Function_8_AD0(): pass

    label("Function_8_AD0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_AE0"),
        (101, "loc_C41"),
        (SWITCH_DEFAULT, "loc_DA2"),
    )


    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_END)), "loc_AE8")
    Return()

    label("loc_AE8")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BDC"),
        (SWITCH_DEFAULT, "loc_BFF"),
    )


    label("loc_BDC")

    Fade(500)
    OP_89(0x0, -148540, 2360, 114080, 156)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_BFF")

    Battle(0xEED, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -148540, 2360, 114080, 156)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_C38"),
        (1, "loc_C3B"),
        (SWITCH_DEFAULT, "loc_C3E"),
    )


    label("loc_C38")

    EventEnd(0x0)
    Return()

    label("loc_C3B")

    OP_B4(0x0)
    Return()

    label("loc_C3E")

    Jump("loc_DA2")

    label("loc_C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 6)), scpexpr(EXPR_END)), "loc_C49")
    Return()

    label("loc_C49")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_D3D"),
        (SWITCH_DEFAULT, "loc_D60"),
    )


    label("loc_D3D")

    Fade(500)
    OP_89(0x0, -148760, 3940, 101000, 18)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_D60")

    Battle(0xEF7, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -148760, 3940, 101000, 18)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_D99"),
        (1, "loc_D9C"),
        (SWITCH_DEFAULT, "loc_D9F"),
    )


    label("loc_D99")

    EventEnd(0x0)
    Return()

    label("loc_D9C")

    OP_B4(0x0)
    Return()

    label("loc_D9F")

    Jump("loc_DA2")

    label("loc_DA2")

    EventBegin(0x1)
    SetChrFlags(0x9, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20F6)
    OP_28(0xB5, 0x4, 0x10)
    OP_28(0xB5, 0x4, 0x2)
    OP_28(0xB5, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_8_AD0 end

    def Function_9_E13(): pass

    label("Function_9_E13")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #17
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
        (0, "loc_E8F"),
        (1, "loc_10E6"),
        (SWITCH_DEFAULT, "loc_114E"),
    )


    label("loc_E8F")

    Battle(0xD3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_EB0"),
        (2, "loc_1066"),
        (1, "loc_10DE"),
        (SWITCH_DEFAULT, "loc_10E3"),
    )


    label("loc_EB0")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F71")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Set as exterminated the wanted monsters at the Amberl Tower and in the Nebel Valley\x01",      # 0
            "No change\x01",                                                                                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F5C"),
        (SWITCH_DEFAULT, "loc_F71"),
    )


    label("loc_F5C")

    OP_A2(0x1A0F)
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0xB3, 0x1, 0x1)
    Jump("loc_F71")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F83")
    Call(0, 10)
    Jump("loc_1063")

    label("loc_F83")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -136150, 4030, 88170, 135)
    SetChrPos(0x1, -136150, 4030, 88170, 135)
    SetChrPos(0x2, -136150, 4030, 88170, 135)
    SetChrPos(0x3, -136150, 4030, 88170, 135)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Exterminated monster at Krone Pass!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1A0E)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x2)
    OP_28(0x93, 0x1, 0x4)
    OP_28(0x93, 0x1, 0x8)
    Sleep(400)

    label("loc_1063")

    Jump("loc_10E3")

    label("loc_1066")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -138230, 4019, 89590, 135)
    SetChrPos(0x1, -138230, 4019, 89590, 135)
    SetChrPos(0x2, -138230, 4019, 89590, 135)
    SetChrPos(0x3, -138230, 4019, 89590, 135)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_10E3")

    label("loc_10DE")

    OP_B4(0x0)
    Jump("loc_10E3")

    label("loc_10E3")

    Jump("loc_114E")

    label("loc_10E6")

    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -138230, 4019, 89590, 135)
    SetChrPos(0x1, -138230, 4019, 89590, 135)
    SetChrPos(0x2, -138230, 4019, 89590, 135)
    SetChrPos(0x3, -138230, 4019, 89590, 135)
    OP_69(0x0, 0x0)
    OP_0D()
    Jump("loc_114E")

    label("loc_114E")

    EventEnd(0x0)
    Return()

    # Function_9_E13 end

    def Function_10_1151(): pass

    label("Function_10_1151")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1164")
    Call(0, 11)

    label("loc_1164")

    OP_6D(-135710, 4050, 87980, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -136610, 4010, 88580, 135)
    SetChrPos(0x106, -136320, 4010, 87160, 45)
    SetChrPos(0xF8, -134790, 4030, 89020, 225)
    SetChrPos(0xF9, -134630, 4000, 87460, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #19
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

    AnonymousTalk(    #20
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
        (0, "loc_1328"),
        (1, "loc_15C0"),
        (2, "loc_1813"),
        (SWITCH_DEFAULT, "loc_1A66"),
    )


    label("loc_1328")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C4")

    ChrTalk(    #21
        0x108,
        (
            "#072FIt was a challenge, but...\x01",
            "the monsters' behavior was odd, as well.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B7")

    label("loc_13C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_146A")

    ChrTalk(    #22
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
    Jump("loc_15B7")

    label("loc_146A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(    #23
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
    Jump("loc_15B7")

    label("loc_1512")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B7")

    ChrTalk(    #24
        0x105,
        (
            "#043FThey were certainly powerful,\x01",
            "but their behavior... It was so odd.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B7")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_1A66")

    label("loc_15C0")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(    #25
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180A")

    label("loc_163D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C1")

    ChrTalk(    #26
        0x103,
        (
            "#022FYes, all of the monsters were acting\x01",
            "strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180A")

    label("loc_16C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1776")

    ChrTalk(    #27
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
    Jump("loc_180A")

    label("loc_1776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180A")

    ChrTalk(    #28
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180A")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_1A66")

    label("loc_1813")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1890")

    ChrTalk(    #29
        0x108,
        (
            "#072FYes, the monsters' behavior was odd.\x02\x03",

            "Some were ready to kill us,\x01",
            "some were ready to flee...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5D")

    label("loc_1890")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1914")

    ChrTalk(    #30
        0x103,
        (
            "#022FYes, all of the monsters were acting strangely.\x02\x03",

            "Some were bizarrely ferocious,\x01",
            "others were panicking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5D")

    label("loc_1914")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C9")

    ChrTalk(    #31
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
    Jump("loc_1A5D")

    label("loc_19C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5D")

    ChrTalk(    #32
        0x105,
        (
            "#042FYes, the behavior of the monsters was...\x01",
            "bizarre.\x02\x03",

            "Some of them were blind with fury,\x01",
            "but others were panicked and fearful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5D")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_1A66")

    label("loc_1A66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB7")

    ChrTalk(    #33
        0x107,
        (
            "#065FI kinda noticed that too.\x02\x03",

            "#561FIt was kinda scary...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B05")

    ChrTalk(    #34
        0x105,
        (
            "#043FI also noticed that.\x02\x03",

            "I wonder what it could mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1B05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B71")

    ChrTalk(    #35
        0x104,
        (
            "#032FI, too, could not help but notice\x01",
            "their confusion.\x02\x03",

            "I wish I knew what it meant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC6")

    ChrTalk(    #36
        0x103,
        (
            "#026FI got the same impression.\x02\x03",

            "#522FMmmm... What could it mean?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC6")


    ChrTalk(    #37
        0x106,
        "#057F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1004FAgate? Something up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        (
            "#555FEh...\x02\x03",

            "Just thinkin' this might be a warning\x01",
            "about somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1020FA warning... You mean to something\x01",
            "Ouroboros is doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
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

    ChrTalk(    #42
        0x101,
        "#1004FRight after...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D64")

    ChrTalk(    #43
        0x107,
        "#063FAgate...?\x02",
    )

    CloseMessageWindow()

    label("loc_1D64")


    ChrTalk(    #44
        0x106,
        (
            "#053FEnough 'bout that.\x02\x03",

            "#057FPoint is, animals have better instincts\x01",
            "about this sorta stuff than us humans do.\x02\x03",

            "We'd better keep our eyes open for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002FYeah...good point.\x02\x03",

            "Back to the guildhouse for us, then,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        "#050FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A0E)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x2)
    OP_28(0x93, 0x1, 0x4)
    OP_28(0x93, 0x1, 0x8)
    OP_28(0x93, 0x1, 0x2000)
    EventEnd(0x0)
    Return()

    # Function_10_1151 end

    def Function_11_1E96(): pass

    label("Function_11_1E96")

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
        (0, "loc_1F4C"),
        (1, "loc_1F52"),
        (SWITCH_DEFAULT, "loc_1F58"),
    )


    label("loc_1F4C")

    OP_A2(0x1200)
    Jump("loc_1F58")

    label("loc_1F52")

    OP_A2(0x1201)
    Jump("loc_1F58")

    label("loc_1F58")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_1E96 end

    SaveToFile()

Try(main)
