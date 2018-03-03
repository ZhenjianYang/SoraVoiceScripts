from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3110   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'ED6_DT07/CH00330 ._CH',             # 00
        'ED6_DT07/CH00331 ._CH',             # 01
        'ED6_DT07/CH00430 ._CH',             # 02
        'ED6_DT07/CH00431 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00330P._CP',             # 00
        'ED6_DT07/CH00331P._CP',             # 01
        'ED6_DT07/CH00430P._CP',             # 02
        'ED6_DT07/CH00431P._CP',             # 03
    )

    DeclMonster(
        X                   = -117810,
        Z                   = 0,
        Y                   = -4690,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -139310,
        Z                   = 0,
        Y                   = 2420,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27330,
        Z                   = 0,
        Y                   = 2970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14900,
        Z                   = 0,
        Y                   = -44370,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69270,
        Z                   = 0,
        Y                   = -22860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 20910,
        TriggerZ            = 0,
        TriggerY            = 262330,
        TriggerRange        = 1000,
        ActorX              = 21000,
        ActorZ              = 3000,
        ActorY              = 263000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -95810,
        TriggerZ            = 0,
        TriggerY            = 3940,
        TriggerRange        = 1000,
        ActorX              = -95810,
        ActorZ              = 1000,
        ActorY              = 3940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -106270,
        TriggerZ            = 0,
        TriggerY            = 4200,
        TriggerRange        = 1000,
        ActorX              = -106270,
        ActorZ              = 1000,
        ActorY              = 4200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121890,
        TriggerZ            = 0,
        TriggerY            = 3090,
        TriggerRange        = 1000,
        ActorX              = -121890,
        ActorZ              = 1000,
        ActorY              = 3090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -129830,
        TriggerZ            = 0,
        TriggerY            = 2950,
        TriggerRange        = 1000,
        ActorX              = -129830,
        ActorZ              = 1000,
        ActorY              = 2950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_21E",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_4A0",          # 03, 3
        "Function_4_5EA",          # 04, 4
        "Function_5_74F",          # 05, 5
        "Function_6_880",          # 06, 6
        "Function_7_8A3",          # 07, 7
        "Function_8_8C6",          # 08, 8
        "Function_9_8E9",          # 09, 9
        "Function_10_90C",         # 0A, 10
        "Function_11_92F",         # 0B, 11
        "Function_12_952",         # 0C, 12
        "Function_13_9AB",         # 0D, 13
        "Function_14_B41",         # 0E, 14
        "Function_15_BF7",         # 0F, 15
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_21D")

    Return()

    # Function_0_20A end

    def Function_1_21E(): pass

    label("Function_1_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_232")
    OP_72(0x101A, 0x0)
    ExitThread()
    OP_6F(0x1A, 80)

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_246")
    OP_72(0x101B, 0x0)
    ExitThread()
    OP_6F(0x1B, 80)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25A")
    OP_72(0x101C, 0x0)
    ExitThread()
    OP_6F(0x1C, 80)

    label("loc_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_26E")
    OP_72(0x101D, 0x0)
    ExitThread()
    OP_6F(0x1D, 80)

    label("loc_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_282")
    OP_72(0x101E, 0x0)
    ExitThread()
    OP_6F(0x1E, 80)

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_296")
    OP_72(0x101F, 0x0)
    ExitThread()
    OP_6F(0x1F, 80)

    label("loc_296")

    OP_1C(0x1A, 0x0, 0x6)
    OP_1C(0x1B, 0x0, 0x7)
    OP_1C(0x1C, 0x0, 0x8)
    OP_1C(0x1D, 0x0, 0x9)
    OP_1C(0x1E, 0x0, 0xA)
    OP_1C(0x1F, 0x0, 0xB)
    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2C7")
    OP_82(0x81, 0x0)
    Jump("loc_2CA")

    label("loc_2C7")

    OP_82(0x82, 0x0)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC")
    OP_6F(0x29, 0)
    Jump("loc_2E3")

    label("loc_2DC")

    OP_6F(0x29, 60)

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    OP_6F(0x2A, 0)
    Jump("loc_2FC")

    label("loc_2F5")

    OP_6F(0x2A, 60)

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E")
    OP_6F(0x2B, 0)
    Jump("loc_315")

    label("loc_30E")

    OP_6F(0x2B, 60)

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_6F(0x2C, 0)
    Jump("loc_32E")

    label("loc_327")

    OP_6F(0x2C, 60)

    label("loc_32E")

    Return()

    # Function_1_21E end

    def Function_2_32F(): pass

    label("Function_2_32F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x335, 1)"), scpexpr(EXPR_END)), "loc_39D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x35\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B84)
    Jump("loc_405")

    label("loc_39D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x35\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x35\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_405")

    Jump("loc_492")

    label("loc_408")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05A small plate of windowglass lies on the bottom of the empty box. Alas,\x01",
            "another unexpected chest pane!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1C, 0x0)

    label("loc_492")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_32F end

    def Function_3_4A0(): pass

    label("Function_3_4A0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A4, 1)"), scpexpr(EXPR_END)), "loc_50E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA4\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B85)
    Jump("loc_576")

    label("loc_50E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA4\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA4\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_576")

    Jump("loc_5DC")

    label("loc_579")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05You realize that was in my stomach until just now, right? Yuck!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1D, 0x0)

    label("loc_5DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4A0 end

    def Function_4_5EA(): pass

    label("Function_4_5EA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_658")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B86)
    Jump("loc_6C0")

    label("loc_658")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_6C0")

    Jump("loc_741")

    label("loc_6C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05Kevin briefly considers taking the chest as a new weapon, but it's not\x01",
            "quite bow-y enough.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1E, 0x0)

    label("loc_741")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5EA end

    def Function_5_74F(): pass

    label("Function_5_74F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_828")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29B, 1)"), scpexpr(EXPR_END)), "loc_7BD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x9B\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B87)
    Jump("loc_825")

    label("loc_7BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x9B\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9B\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_825")

    Jump("loc_872")

    label("loc_828")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Thieving attempt failed! -20 Charisma.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x1F, 0x0)

    label("loc_872")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_74F end

    def Function_6_880(): pass

    label("Function_6_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A2")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x0)
    OP_72(0x21A, 0x0)
    ExitThread()
    OP_72(0x101A, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_8A2")

    Return()

    # Function_6_880 end

    def Function_7_8A3(): pass

    label("Function_7_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x1)
    OP_72(0x21B, 0x0)
    ExitThread()
    OP_72(0x101B, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_8C5")

    Return()

    # Function_7_8A3 end

    def Function_8_8C6(): pass

    label("Function_8_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x2)
    OP_72(0x21C, 0x0)
    ExitThread()
    OP_72(0x101C, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_8E8")

    Return()

    # Function_8_8C6 end

    def Function_9_8E9(): pass

    label("Function_9_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90B")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21D, 0x0)
    ExitThread()
    OP_72(0x101D, 0x0)
    ExitThread()
    OP_A2(0x3)
    TalkEnd(0xFF)

    label("loc_90B")

    Return()

    # Function_9_8E9 end

    def Function_10_90C(): pass

    label("Function_10_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92E")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21E, 0x0)
    ExitThread()
    OP_72(0x101E, 0x0)
    ExitThread()
    OP_A2(0x4)
    TalkEnd(0xFF)

    label("loc_92E")

    Return()

    # Function_10_90C end

    def Function_11_92F(): pass

    label("Function_11_92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_951")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21F, 0x0)
    ExitThread()
    OP_72(0x101F, 0x0)
    ExitThread()
    OP_A2(0x5)
    TalkEnd(0xFF)

    label("loc_951")

    Return()

    # Function_11_92F end

    def Function_12_952(): pass

    label("Function_12_952")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_12_952 end

    def Function_13_9AB(): pass

    label("Function_13_9AB")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 21610, 0, 260060, 0)
    SetChrPos(0x1, 20020, 0, 260000, 0)
    SetChrPos(0x2, 21370, 0, 258140, 0)
    SetChrPos(0x3, 19670, 0, 258010, 0)
    OP_6D(19670, 0, 258010, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3910, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A81")
    OP_28(0xE, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_A81")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        (
            "\x07\x05#40WBring to me the repenting patriot.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B35")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B32")
    Call(0, 14)

    label("loc_B32")

    Jump("loc_B35")

    label("loc_B35")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_13_9AB end

    def Function_14_B41(): pass

    label("Function_14_B41")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_70(0x28, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x28)
    Sleep(500)

    def lambda_BAA():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BAA)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x14, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_B41 end

    def Function_15_BF7(): pass

    label("Function_15_BF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 21610, 0, 260060, 0)
    SetChrPos(0x1, 20020, 0, 260000, 0)
    SetChrPos(0x2, 21370, 0, 258140, 0)
    SetChrPos(0x3, 19670, 0, 258010, 0)
    OP_6D(19670, 0, 258010, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3910, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_15_BF7 end

    SaveToFile()

Try(main)
