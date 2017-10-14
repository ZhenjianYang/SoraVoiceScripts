from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1305   ._SN',
        MapName             = 'Bose',
        Location            = 'C1305.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        'Major Vander',                         # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
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
        'ED6_DT09/CH10380 ._CH',             # 00
        'ED6_DT09/CH10381 ._CH',             # 01
        'ED6_DT09/CH10390 ._CH',             # 02
        'ED6_DT09/CH10391 ._CH',             # 03
        'ED6_DT09/CH10250 ._CH',             # 04
        'ED6_DT09/CH10251 ._CH',             # 05
        'ED6_DT07/CH00330 ._CH',             # 06
        'ED6_DT07/CH00331 ._CH',             # 07
        'ED6_DT27/CH03570 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT09/CH10380P._CP',             # 00
        'ED6_DT09/CH10381P._CP',             # 01
        'ED6_DT09/CH10390P._CP',             # 02
        'ED6_DT09/CH10391P._CP',             # 03
        'ED6_DT09/CH10250P._CP',             # 04
        'ED6_DT09/CH10251P._CP',             # 05
        'ED6_DT07/CH00330P._CP',             # 06
        'ED6_DT07/CH00331P._CP',             # 07
        'ED6_DT27/CH03570P._CP',             # 08
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


    DeclMonster(
        X                   = -5080,
        Z                   = 0,
        Y                   = 890,
        Unknown_0C          = 133,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 65660,
        Z                   = 0,
        Y                   = -21310,
        Unknown_0C          = 167,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -117030,
        Z                   = 0,
        Y                   = -197030,
        Unknown_0C          = 355,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -164160,
        TriggerZ            = 0,
        TriggerY            = -193160,
        TriggerRange        = 1000,
        ActorX              = -164160,
        ActorZ              = 1500,
        ActorY              = -193160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54870,
        TriggerZ            = 0,
        TriggerY            = 46490,
        TriggerRange        = 1000,
        ActorX              = -54740,
        ActorZ              = 1500,
        ActorY              = 47090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -206690,
        TriggerZ            = 0,
        TriggerY            = -155420,
        TriggerRange        = 1000,
        ActorX              = -206660,
        ActorZ              = 1500,
        ActorY              = -154670,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4600,
        TriggerZ            = 0,
        TriggerY            = 41900,
        TriggerRange        = 1000,
        ActorX              = 5290,
        ActorZ              = 0,
        ActorY              = 42020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4550,
        TriggerZ            = 0,
        TriggerY            = 83030,
        TriggerRange        = 1000,
        ActorX              = 5170,
        ActorZ              = 0,
        ActorY              = 82970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54600,
        TriggerZ            = 0,
        TriggerY            = 41990,
        TriggerRange        = 1000,
        ActorX              = 55250,
        ActorZ              = 0,
        ActorY              = 41960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -51050,
        TriggerZ            = 0,
        TriggerY            = -136510,
        TriggerRange        = 800,
        ActorX              = -51050,
        ActorZ              = 800,
        ActorY              = -136510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_262",          # 00, 0
        "Function_1_28F",          # 01, 1
        "Function_2_347",          # 02, 2
        "Function_3_475",          # 03, 3
        "Function_4_60A",          # 04, 4
        "Function_5_75D",          # 05, 5
        "Function_6_87F",          # 06, 6
        "Function_7_9D8",          # 07, 7
        "Function_8_B07",          # 08, 8
        "Function_9_B95",          # 09, 9
        "Function_10_CE1",         # 0A, 10
        "Function_11_CFE",         # 0B, 11
    )


    def Function_0_262(): pass

    label("Function_0_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_27C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 11)
    Jump("loc_28E")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_28E")
    OP_64(0x6, 0x1)
    OP_A3(0x10F1)
    Event(0, 9)

    label("loc_28E")

    Return()

    # Function_0_262 end

    def Function_1_28F(): pass

    label("Function_1_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1")
    OP_6F(0x1, 0)
    Jump("loc_2A8")

    label("loc_2A1")

    OP_6F(0x1, 60)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA")
    OP_6F(0x2, 0)
    Jump("loc_2C1")

    label("loc_2BA")

    OP_6F(0x2, 60)

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D3")
    OP_6F(0x3, 0)
    Jump("loc_2DA")

    label("loc_2D3")

    OP_6F(0x3, 60)

    label("loc_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x4, 0)
    Jump("loc_2F3")

    label("loc_2EC")

    OP_6F(0x4, 60)

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305")
    OP_6F(0x5, 0)
    Jump("loc_30C")

    label("loc_305")

    OP_6F(0x5, 60)

    label("loc_30C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E")
    OP_6F(0x6, 0)
    Jump("loc_325")

    label("loc_31E")

    OP_6F(0x6, 60)

    label("loc_325")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 1)), scpexpr(EXPR_END)), "loc_33D")
    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Jump("loc_346")

    label("loc_33D")

    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_346")

    Return()

    # Function_1_28F end

    def Function_2_347(): pass

    label("Function_2_347")

    OP_EA(0x2, 0x4A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3B8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1904)
    Jump("loc_41C")

    label("loc_3B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_41C")

    Jump("loc_467")

    label("loc_41F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Was returning here another...BRIGHT IDEA?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_467")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_347 end

    def Function_3_475(): pass

    label("Function_3_475")

    OP_EA(0x2, 0x4B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_4E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1905)
    Jump("loc_54A")

    label("loc_4E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_54A")

    Jump("loc_5FC")

    label("loc_54D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Unable to see the bottom of this ostensibly\x01",
            "empty chest, you drop a pebble into it. You don't\x01",
            "hear it hit the bottom. ...Probably best to leave.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_475 end

    def Function_4_60A(): pass

    label("Function_4_60A")

    OP_EA(0x2, 0x4C, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_67B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1906)
    Jump("loc_6DF")

    label("loc_67B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_6DF")

    Jump("loc_74F")

    label("loc_6E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05When you gaze long enough into the empty\x01",
            "chest, the chest gazes back into you.\x07\x00\x02",
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

    # Function_4_60A end

    def Function_5_75D(): pass

    label("Function_5_75D")

    OP_EA(0x2, 0x4D, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x320, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_835")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_7CE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1907)
    Jump("loc_832")

    label("loc_7CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_832")

    Jump("loc_871")

    label("loc_835")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Aw, man! Nothing AGAIN? Geez.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_871")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_75D end

    def Function_6_87F(): pass

    label("Function_6_87F")

    OP_EA(0x2, 0x4E, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_957")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_8F0")
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
    OP_A2(0x1908)
    Jump("loc_954")

    label("loc_8F0")

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
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_954")

    Jump("loc_9CA")

    label("loc_957")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05This chest is as empty as my well of creativity\x01",
            "after writing all of these messages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9CA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_87F end

    def Function_7_9D8(): pass

    label("Function_7_9D8")

    OP_EA(0x2, 0x4F, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x321, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A49")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1909)
    Jump("loc_AAD")

    label("loc_A49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_AAD")

    Jump("loc_AF9")

    label("loc_AB0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05You obtain the Emperor's New Clothes. Not.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AF9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_9D8 end

    def Function_8_B07(): pass

    label("Function_8_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")
    EventBegin(0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_B94")

    label("loc_B20")


    ChrTalk(    #18
        0x102,
        (
            "#1030F(Looks like they're dining.)\x02\x03",

            "(They probably won't be getting up for a while.\x01",
            "Let's just sneak past.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_B94")

    Return()

    # Function_8_B07 end

    def Function_9_B95(): pass

    label("Function_9_B95")

    EventBegin(0x0)
    SetChrPos(0x102, -50940, 0, -136720, 0)
    SetChrPos(0x146, -51350, 0, -138260, 0)
    SetChrPos(0x129, -50230, 0, -138010, 0)
    SetChrPos(0x12A, -52460, 0, -137530, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0x102,
        "#1033F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x146,
        (
            "#213F#6PHmm?\x02\x03",

            "(Joshua, what's up?)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 500)
    Sleep(300)

    ChrTalk(    #21
        0x102,
        (
            "#1031F(Oh... The people within are eating.)\x02\x03",

            "(They probably won't be getting up for\x01",
            "a while, so let's just sneak past.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x146,
        "#210F#6P(Got it.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x129,
        "#490F(Let's keep moving.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1803)
    OP_65(0x6, 0x1)
    EventEnd(0x0)
    Return()

    # Function_9_B95 end

    def Function_10_CE1(): pass

    label("Function_10_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 1)), scpexpr(EXPR_END)), "loc_CF4")
    NewScene("ED6_DT21/C1300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_CFD")

    label("loc_CF4")

    NewScene("ED6_DT21/C1301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_CFD")

    Return()

    # Function_10_CE1 end

    def Function_11_CFE(): pass

    label("Function_11_CFE")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(2320, 1750, -19320, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 7500, 3500, -20200, 270)
    ClearChrFlags(0x8, 0x80)

    def lambda_D6D():
        OP_8E(0x8, 0x50A, 0x0, 0xFFFFB118, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_D6D)
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 0x0)
    Sleep(500)

    ChrTalk(    #24
        0x8,
        (
            "#272F#5PI wonder which of us really 'escaped,'\x01",
            "here.\x02\x03",

            "#275FI'm greener than I thought, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #25
        0x8,
        (
            "#276F#5PEven so... Hamel, hmm?\x02\x03",

            "Seems I've no choice but to help him\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    NewScene("ED6_DT21/E0001   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_11_CFE end

    SaveToFile()

Try(main)
