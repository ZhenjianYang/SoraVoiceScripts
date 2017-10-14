from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3601   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        'ED6_DT29/CH12660 ._CH',             # 00
        'ED6_DT29/CH12661 ._CH',             # 01
        'ED6_DT29/CH12670 ._CH',             # 02
        'ED6_DT29/CH12671 ._CH',             # 03
        'ED6_DT29/CH12680 ._CH',             # 04
        'ED6_DT29/CH12681 ._CH',             # 05
        'ED6_DT29/CH12690 ._CH',             # 06
        'ED6_DT29/CH12691 ._CH',             # 07
        'ED6_DT29/CH12700 ._CH',             # 08
        'ED6_DT29/CH12701 ._CH',             # 09
        'ED6_DT29/CH12710 ._CH',             # 0A
        'ED6_DT29/CH12711 ._CH',             # 0B
        'ED6_DT29/CH12720 ._CH',             # 0C
        'ED6_DT29/CH12721 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12660P._CP',             # 00
        'ED6_DT29/CH12661P._CP',             # 01
        'ED6_DT29/CH12670P._CP',             # 02
        'ED6_DT29/CH12671P._CP',             # 03
        'ED6_DT29/CH12680P._CP',             # 04
        'ED6_DT29/CH12681P._CP',             # 05
        'ED6_DT29/CH12690P._CP',             # 06
        'ED6_DT29/CH12691P._CP',             # 07
        'ED6_DT29/CH12700P._CP',             # 08
        'ED6_DT29/CH12701P._CP',             # 09
        'ED6_DT29/CH12710P._CP',             # 0A
        'ED6_DT29/CH12711P._CP',             # 0B
        'ED6_DT29/CH12720P._CP',             # 0C
        'ED6_DT29/CH12721P._CP',             # 0D
    )

    DeclNpc(
        X                   = -20,
        Z                   = 1000,
        Y                   = -31930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 18090,
        Z                   = 4400,
        Y                   = 14060,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7861,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1910,
        Z                   = 4400,
        Y                   = -18170,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7862,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33620,
        Z                   = 400,
        Y                   = 17700,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7863,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 18030,
        TriggerZ            = 4400,
        TriggerY            = 7080,
        TriggerRange        = 1000,
        ActorX              = 18030,
        ActorZ              = 4400,
        ActorY              = 6460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12960,
        TriggerZ            = -3600,
        TriggerY            = 18020,
        TriggerRange        = 1000,
        ActorX              = 12260,
        ActorZ              = -3600,
        ActorY              = 18010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = -50,
        TriggerY            = -31270,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = -50,
        ActorY              = -31930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6850,
        TriggerZ            = 400,
        TriggerY            = -31890,
        TriggerRange        = 1000,
        ActorX              = 7560,
        ActorZ              = 400,
        ActorY              = -31890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 400,
        TriggerY            = -38890,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = 400,
        ActorY              = -39510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6950,
        TriggerZ            = 400,
        TriggerY            = -31950,
        TriggerRange        = 1000,
        ActorX              = -7610,
        ActorZ              = 400,
        ActorY              = -31950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_29B",          # 01, 1
        "Function_2_392",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_4C1",          # 04, 4
        "Function_5_5FD",          # 05, 5
        "Function_6_7FD",          # 06, 6
        "Function_7_970",          # 07, 7
        "Function_8_B05",          # 08, 8
        "Function_9_C74",          # 09, 9
        "Function_10_D74",         # 0A, 10
        "Function_11_DEC",         # 0B, 11
        "Function_12_EEC",         # 0C, 12
        "Function_13_F64",         # 0D, 13
        "Function_14_1064",        # 0E, 14
        "Function_15_10DC",        # 0F, 15
        "Function_16_11DC",        # 10, 16
        "Function_17_1254",        # 11, 17
        "Function_18_1333",        # 12, 18
        "Function_19_1412",        # 13, 19
        "Function_20_1460",        # 14, 20
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_27E"),
        (101, "loc_285"),
        (102, "loc_28C"),
        (103, "loc_293"),
        (SWITCH_DEFAULT, "loc_29A"),
    )


    label("loc_27E")

    Event(0, 9)
    Jump("loc_29A")

    label("loc_285")

    Event(0, 11)
    Jump("loc_29A")

    label("loc_28C")

    Event(0, 13)
    Jump("loc_29A")

    label("loc_293")

    Event(0, 15)
    Jump("loc_29A")

    label("loc_29A")

    Return()

    # Function_0_266 end

    def Function_1_29B(): pass

    label("Function_1_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_6F(0x0, 0)
    Jump("loc_2B4")

    label("loc_2AD")

    OP_6F(0x0, 60)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_6F(0x1, 0)
    Jump("loc_2CD")

    label("loc_2C6")

    OP_6F(0x1, 60)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF")
    OP_6F(0x2, 0)
    Jump("loc_2E6")

    label("loc_2DF")

    OP_6F(0x2, 60)

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8")
    OP_6F(0x3, 0)
    Jump("loc_2FF")

    label("loc_2F8")

    OP_6F(0x3, 60)

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311")
    OP_6F(0x4, 0)
    Jump("loc_318")

    label("loc_311")

    OP_6F(0x4, 60)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A")
    OP_6F(0x5, 0)
    Jump("loc_331")

    label("loc_32A")

    OP_6F(0x5, 60)

    label("loc_331")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 5)), scpexpr(EXPR_END)), "loc_365")
    SetChrFlags(0x9, 0x80)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 6)), scpexpr(EXPR_END)), "loc_371")
    SetChrFlags(0xA, 0x80)

    label("loc_371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 7)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0xB, 0x80)

    label("loc_37D")

    OP_1B(0x0, 0x0, 0xA)
    OP_1B(0x1, 0x0, 0xC)
    OP_1B(0x2, 0x0, 0xE)
    OP_1B(0x3, 0x0, 0x10)
    Return()

    # Function_1_29B end

    def Function_2_392(): pass

    label("Function_2_392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_392")

    label("loc_3A7")

    Return()

    # Function_2_392 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    OP_EA(0x2, 0xDC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_419")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F30)
    Jump("loc_47D")

    label("loc_419")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_47D")

    Jump("loc_4B3")

    label("loc_480")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Nothing but nothing.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3A8 end

    def Function_4_4C1(): pass

    label("Function_4_4C1")

    OP_EA(0x2, 0xDD, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_532")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F31)
    Jump("loc_596")

    label("loc_532")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_596")

    Jump("loc_5EF")

    label("loc_599")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05There is nothing in the chest. NOTHING.\x01",
            "Now shoo. Shoo!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4C1 end

    def Function_5_5FD(): pass

    label("Function_5_5FD")

    OP_EA(0x2, 0xDE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_654():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_654)

    def lambda_66F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_66F)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #6
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x418, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6C2"),
        (2, "loc_6D4"),
        (1, "loc_6E4"),
        (SWITCH_DEFAULT, "loc_6E7"),
    )


    label("loc_6C2")

    OP_A2(0x1F33)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_6E7")

    label("loc_6D4")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6E4")

    OP_B4(0x0)
    Return()

    label("loc_6E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x143, 1)"), scpexpr(EXPR_END)), "loc_733")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "Found \x1F\x43\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F32)
    Jump("loc_795")

    label("loc_733")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "Found \x1F\x43\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x43\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_795")

    Jump("loc_7EF")

    label("loc_798")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        (
            "\x07\x05Sure, it's empty now, but maybe if you\x01",
            "checked it again...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5FD end

    def Function_6_7FD(): pass

    label("Function_6_7FD")

    OP_EA(0x2, 0xDF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_86E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x01\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F34)
    Jump("loc_8D2")

    label("loc_86E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
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

    label("loc_8D2")

    Jump("loc_962")

    label("loc_8D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05As you search the empty chest's insides,\x01",
            "just in case you missed something last time,\x01",
            "it gives you a splinter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_962")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7FD end

    def Function_7_970(): pass

    label("Function_7_970")

    OP_EA(0x2, 0xE0, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_9E1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\xFA\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F35)
    Jump("loc_A45")

    label("loc_9E1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\xFA\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFA\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A45")

    Jump("loc_AF7")

    label("loc_A48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05You lift the chest over your head and shake as\x01",
            "hard as you can, but nothing comes out. Well,\x01",
            "it was an impressive display of strength, at least.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AF7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_970 end

    def Function_8_B05(): pass

    label("Function_8_B05")

    OP_EA(0x2, 0xE1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B76")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\xF9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F36)
    Jump("loc_BDA")

    label("loc_B76")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "Found \x1F\xF9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_BDA")

    Jump("loc_C66")

    label("loc_BDD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05You see a single tear roll down its treasure chest\x01",
            "cheek. Wait a second... Chests don't have tear\x01",
            "ducts...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B05 end

    def Function_9_C74(): pass

    label("Function_9_C74")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x101, 500, 190, 33780, 180)
    SetChrPos(0x102, -500, 190, 33780, 180)
    SetChrPos(0xF8, 500, 190, 34780, 180)
    SetChrPos(0xF9, -500, 190, 34780, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 17)
    Call(0, 19)
    Fade(500)
    OP_6D(-90, 190, 32189, 0)
    SetChrPos(0x0, -90, 190, 32189, 180)
    SetChrPos(0x1, -90, 190, 32189, 180)
    SetChrPos(0x2, -90, 190, 32189, 180)
    SetChrPos(0x3, -90, 190, 32189, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_9_C74 end

    def Function_10_D74(): pass

    label("Function_10_D74")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x101, -500, 190, 34780, 0)
    SetChrPos(0x102, 500, 190, 34780, 0)
    SetChrPos(0xF8, -500, 190, 33780, 0)
    SetChrPos(0xF9, 500, 190, 33780, 0)
    OP_0D()
    Call(0, 17)
    Call(0, 20)
    NewScene("ED6_DT21/C3600   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_10_D74 end

    def Function_11_DEC(): pass

    label("Function_11_DEC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x101, 34500, 190, 130, 180)
    SetChrPos(0x102, 33500, 190, 130, 180)
    SetChrPos(0xF8, 34500, 190, 1130, 180)
    SetChrPos(0xF9, 33500, 190, 1130, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(34000, 190, -1740, 0)
    SetChrPos(0x0, 34000, 190, -1740, 180)
    SetChrPos(0x1, 34000, 190, -1740, 180)
    SetChrPos(0x2, 34000, 190, -1740, 180)
    SetChrPos(0x3, 34000, 190, -1740, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_11_DEC end

    def Function_12_EEC(): pass

    label("Function_12_EEC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x101, 33500, 190, 1130, 0)
    SetChrPos(0x102, 34500, 190, 1130, 0)
    SetChrPos(0xF8, 33500, 190, 130, 0)
    SetChrPos(0xF9, 34500, 190, 130, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_EEC end

    def Function_13_F64(): pass

    label("Function_13_F64")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 190, 500, 0)
    SetChrPos(0x101, 500, 190, 0, 180)
    SetChrPos(0x102, -500, 190, 0, 180)
    SetChrPos(0xF8, 500, 190, 1000, 180)
    SetChrPos(0xF9, -500, 190, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(130, 190, -1790, 0)
    SetChrPos(0x0, 130, 190, -1790, 180)
    SetChrPos(0x1, 130, 190, -1790, 180)
    SetChrPos(0x2, 130, 190, -1790, 180)
    SetChrPos(0x3, 130, 190, -1790, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_13_F64 end

    def Function_14_1064(): pass

    label("Function_14_1064")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 190, 500, 0)
    SetChrPos(0x101, -500, 190, 1000, 0)
    SetChrPos(0x102, 500, 190, 1000, 0)
    SetChrPos(0xF8, -500, 190, 0, 0)
    SetChrPos(0xF9, 500, 190, 0, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1064 end

    def Function_15_10DC(): pass

    label("Function_15_10DC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x101, -33500, 190, 0, 180)
    SetChrPos(0x102, -34500, 190, 0, 180)
    SetChrPos(0xF8, -33500, 190, 1000, 180)
    SetChrPos(0xF9, -34500, 190, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(-33710, 190, -1710, 0)
    SetChrPos(0x0, -33710, 190, -1710, 180)
    SetChrPos(0x1, -33710, 190, -1710, 180)
    SetChrPos(0x2, -33710, 190, -1710, 180)
    SetChrPos(0x3, -33710, 190, -1710, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_15_10DC end

    def Function_16_11DC(): pass

    label("Function_16_11DC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x101, -34500, 190, 1000, 0)
    SetChrPos(0x102, -33500, 190, 1000, 0)
    SetChrPos(0xF8, -34500, 190, 0, 0)
    SetChrPos(0xF9, -33500, 190, 0, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_16_11DC end

    def Function_17_1254(): pass

    label("Function_17_1254")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_17_1254 end

    def Function_18_1333(): pass

    label("Function_18_1333")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_18_1333 end

    def Function_19_1412(): pass

    label("Function_19_1412")


    def lambda_1418():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1418)

    def lambda_142A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_142A)

    def lambda_143C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_143C)

    def lambda_144E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_144E)
    Sleep(2500)
    Return()

    # Function_19_1412 end

    def Function_20_1460(): pass

    label("Function_20_1460")


    def lambda_1466():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1466)

    def lambda_1478():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1478)

    def lambda_148A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_148A)

    def lambda_149C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_149C)
    Sleep(2000)
    Return()

    # Function_20_1460 end

    SaveToFile()

Try(main)
