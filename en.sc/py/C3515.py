from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3515   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3515.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
    )

    DeclNpc(
        X                   = -8980,
        Z                   = 1000,
        Y                   = -8790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -10,
        Z                   = 0,
        Y                   = 20060,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F8,
        Unknown_18          = 5522,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12470,
        Z                   = 0,
        Y                   = -90,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F7,
        Unknown_18          = 5523,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12450,
        Z                   = 0,
        Y                   = -40,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1F6,
        Unknown_18          = 5524,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 9470,
        TriggerZ            = 0,
        TriggerY            = 8330,
        TriggerRange        = 1000,
        ActorX              = 9000,
        ActorZ              = 0,
        ActorY              = 8800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17550,
        TriggerZ            = 0,
        TriggerY            = -12440,
        TriggerRange        = 1000,
        ActorX              = 17180,
        ActorZ              = 0,
        ActorY              = -12940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9430,
        TriggerZ            = 0,
        TriggerY            = -8330,
        TriggerRange        = 1000,
        ActorX              = -8980,
        ActorZ              = 0,
        ActorY              = -8790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12360,
        TriggerZ            = 0,
        TriggerY            = -17620,
        TriggerRange        = 1000,
        ActorX              = -12880,
        ActorZ              = 0,
        ActorY              = -17210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9380,
        TriggerZ            = 0,
        TriggerY            = -8320,
        TriggerRange        = 1000,
        ActorX              = 8970,
        ActorZ              = 0,
        ActorY              = -8790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9250,
        TriggerZ            = 0,
        TriggerY            = 8430,
        TriggerRange        = 1000,
        ActorX              = -8800,
        ActorZ              = 0,
        ActorY              = 8880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_237",          # 01, 1
        "Function_2_304",          # 02, 2
        "Function_3_31A",          # 03, 3
        "Function_4_4B4",          # 04, 4
        "Function_5_646",          # 05, 5
        "Function_6_829",          # 06, 6
        "Function_7_953",          # 07, 7
        "Function_8_A97",          # 08, 8
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Return()

    # Function_0_236 end

    def Function_1_237(): pass

    label("Function_1_237")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)

    label("loc_249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B")
    OP_6F(0x0, 0)
    Jump("loc_262")

    label("loc_25B")

    OP_6F(0x0, 60)

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274")
    OP_6F(0x1, 0)
    Jump("loc_27B")

    label("loc_274")

    OP_6F(0x1, 60)

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D")
    OP_6F(0x2, 0)
    Jump("loc_294")

    label("loc_28D")

    OP_6F(0x2, 60)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6")
    OP_6F(0x3, 0)
    Jump("loc_2AD")

    label("loc_2A6")

    OP_6F(0x3, 60)

    label("loc_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF")
    OP_6F(0x4, 0)
    Jump("loc_2C6")

    label("loc_2BF")

    OP_6F(0x4, 60)

    label("loc_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8")
    OP_6F(0x5, 0)
    Jump("loc_2DF")

    label("loc_2D8")

    OP_6F(0x5, 60)

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B2, 2)), scpexpr(EXPR_END)), "loc_2EB")
    SetChrFlags(0x9, 0x80)

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B2, 3)), scpexpr(EXPR_END)), "loc_2F7")
    SetChrFlags(0xA, 0x80)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B2, 4)), scpexpr(EXPR_END)), "loc_303")
    SetChrFlags(0xB, 0x80)

    label("loc_303")

    Return()

    # Function_1_237 end

    def Function_2_304(): pass

    label("Function_2_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_304")

    label("loc_319")

    Return()

    # Function_2_304 end

    def Function_3_31A(): pass

    label("Function_3_31A")

    OP_EA(0x2, 0xCF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x178, 1)"), scpexpr(EXPR_END)), "loc_38B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x78\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x154B)
    Jump("loc_3EF")

    label("loc_38B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x78\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x78\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3EF")

    Jump("loc_4A6")

    label("loc_3F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You find a whole bunch of caterpillars. They're\x01",
            "kinda crawly and gross, but they'll grow up into\x01",
            "butterflies! Or moths. Moths are kinda gross, too...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_31A end

    def Function_4_4B4(): pass

    label("Function_4_4B4")

    OP_EA(0x2, 0xD0, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x169, 1)"), scpexpr(EXPR_END)), "loc_525")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x69\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x154D)
    Jump("loc_589")

    label("loc_525")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x69\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x69\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_589")

    Jump("loc_638")

    label("loc_58C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05I know it's not much fun to open an empty chest,\x01",
            "but think about how much fun it was to open\x01",
            "when it still had something in it! Ah, memories.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_638")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4B4 end

    def Function_5_646(): pass

    label("Function_5_646")

    OP_EA(0x2, 0xD1, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_69D():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_69D)

    def lambda_6B8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6B8)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #6
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_70B"),
        (2, "loc_71D"),
        (1, "loc_72D"),
        (SWITCH_DEFAULT, "loc_730"),
    )


    label("loc_70B")

    OP_A2(0x1550)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_730")

    label("loc_71D")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_72D")

    OP_B4(0x0)
    Return()

    label("loc_730")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x260, 1)"), scpexpr(EXPR_END)), "loc_77C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "Found \x1F\x60\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x154F)
    Jump("loc_7DE")

    label("loc_77C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "Found \x1F\x60\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x60\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_7DE")

    Jump("loc_81B")

    label("loc_7E1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05No freebies here, I'm afraid.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_81B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_646 end

    def Function_6_829(): pass

    label("Function_6_829")

    OP_EA(0x2, 0xD2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_901")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15F, 1)"), scpexpr(EXPR_END)), "loc_89A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x5F\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1551)
    Jump("loc_8FE")

    label("loc_89A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x5F\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5F\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_8FE")

    Jump("loc_945")

    label("loc_901")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Emptiness, as far as the eye can see.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_945")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_829 end

    def Function_7_953(): pass

    label("Function_7_953")

    OP_EA(0x2, 0xD3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_9C4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1553)
    Jump("loc_A28")

    label("loc_9C4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A28")

    Jump("loc_A89")

    label("loc_A2B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05The chest is empty now. So empty. So lonely.\x01",
            "Please don't go...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A89")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_953 end

    def Function_8_A97(): pass

    label("Function_8_A97")

    OP_EA(0x2, 0xD4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17, 1)"), scpexpr(EXPR_END)), "loc_B08")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\x17\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1554)
    Jump("loc_B6C")

    label("loc_B08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "Found \x1F\x17\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x17\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_B6C")

    Jump("loc_C23")

    label("loc_B6F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05This chest is holding a beauty pageant with all its\x01",
            "other treasure chest friends. But beauty on the\x01",
            "outside can't save how empty it is on the inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C23")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A97 end

    SaveToFile()

Try(main)
