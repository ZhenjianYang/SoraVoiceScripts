from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '',                                     # 16
        '',                                     # 17
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclMonster(
        X                   = 1040,
        Z                   = 0,
        Y                   = 33740,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13230,
        Z                   = 0,
        Y                   = 63010,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24830,
        Z                   = 0,
        Y                   = 62910,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -71240,
        Z                   = 0,
        Y                   = 42750,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -75480,
        Z                   = 0,
        Y                   = -690,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32930,
        Z                   = 0,
        Y                   = -57110,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20530,
        Z                   = 0,
        Y                   = -113240,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 280,
        Z                   = 0,
        Y                   = -131490,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14700,
        Z                   = 0,
        Y                   = -124590,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -74020,
        TriggerZ            = 0,
        TriggerY            = -15990,
        TriggerRange        = 1000,
        ActorX              = -74020,
        ActorZ              = 1500,
        ActorY              = -16720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12830,
        TriggerZ            = 0,
        TriggerY            = -124920,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1500,
        ActorY              = -124890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22010,
        TriggerZ            = 0,
        TriggerY            = -124520,
        TriggerRange        = 1000,
        ActorX              = 21700,
        ActorZ              = 1500,
        ActorY              = -125270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_2B5",          # 01, 1
        "Function_2_306",          # 02, 2
        "Function_3_60D",          # 03, 3
        "Function_4_764",          # 04, 4
        "Function_5_8AA",          # 05, 5
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_29E"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B1")
    OP_A2(0x65B)
    Event(0, 2)

    label("loc_2B1")

    Jump("loc_2B4")

    label("loc_2B4")

    Return()

    # Function_0_292 end

    def Function_1_2B5(): pass

    label("Function_1_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7")
    OP_6F(0x0, 0)
    Jump("loc_2CE")

    label("loc_2C7")

    OP_6F(0x0, 60)

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0")
    OP_6F(0x1, 0)
    Jump("loc_2E7")

    label("loc_2E0")

    OP_6F(0x1, 60)

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9")
    OP_6F(0x2, 0)
    Jump("loc_300")

    label("loc_2F9")

    OP_6F(0x2, 60)

    label("loc_300")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_2B5 end

    def Function_2_306(): pass

    label("Function_2_306")

    EventBegin(0x0)
    OP_6D(2390, 500, 6540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x104, 2810, 1750, 7840, 180)
    SetChrPos(0x108, 3280, 2000, 9470, 180)
    SetChrPos(0x102, 2460, 2000, 9480, 180)

    def lambda_37E():

        label("loc_37E")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_37E")

    QueueWorkItem2(0x108, 1, lambda_37E)

    def lambda_38F():

        label("loc_38F")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_38F")

    QueueWorkItem2(0x102, 1, lambda_38F)

    def lambda_3A0():
        OP_8E(0xFE, 0xA0A, 0x0, 0x16E4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A0)

    def lambda_3BB():
        OP_8E(0xFE, 0xA0A, 0x0, 0x16E4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BB)

    def lambda_3D6():
        OP_8E(0xFE, 0xC94, 0x0, 0x11A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3D6)
    WaitChrThread(0x104, 0x1)

    def lambda_3F6():
        OP_8E(0xFE, 0x3A2, 0x0, 0x132E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F6)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 90, 400)
    WaitChrThread(0x108, 0x2)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #0
        0x104,
        (
            "#030FNow, let's see...\x02\x03",

            "I believe it would be in our best\x01",
            "interests to confirm the location\x01",
            "of the secret waterway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#012F#5PYou're right...\x01",
            "Please, wait a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40026, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(50, 0, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #2
        (
            "\x07\x00#070FWe're currently at this staircase\x01",
            "mark here, on the lower-left...\x02\x03",

            "And the entrance to the hidden\x01",
            "waterway is where the '=' mark\x01",
            "is depicted, in the center.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 0, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #3
        (
            "#012FRight...\x02\x03",

            "So first, we need to go to that\x01",
            "spot and examine the wall.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_28(0x4D, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_2_306 end

    def Function_3_60D(): pass

    label("Function_3_60D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A8, 1)"), scpexpr(EXPR_END)), "loc_68C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00Found \x07\x02Chomping Spare Rib\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6CF)
    Jump("loc_714")

    label("loc_68C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x00Found \x07\x02Chomping Spare Rib\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Chomping Spare Rib\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_714")

    Jump("loc_756")

    label("loc_717")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05The chest is so empty it hurts.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x40)

    label("loc_756")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_60D end

    def Function_4_764(): pass

    label("Function_4_764")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_7DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D0)
    Jump("loc_853")

    label("loc_7DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_853")

    Jump("loc_89C")

    label("loc_856")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05The chest is empty. Are you surprised?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x41)

    label("loc_89C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_764 end

    def Function_5_8AA(): pass

    label("Function_5_8AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_921")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D1)
    Jump("loc_999")

    label("loc_921")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_999")

    Jump("loc_9E3")

    label("loc_99C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        "\x07\x05Don't be shocked now, but...it's empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x42)

    label("loc_9E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8AA end

    SaveToFile()

Try(main)
