from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5505   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5505.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '基尔巴特',                             # 9
        '情绪表现用暂定物体',                   # 10
        '鼠人',                                 # 11
        '鼠人',                                 # 12
        '鼠人',                                 # 13
        '鼠人',                                 # 14
        '鼠人',                                 # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
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
        'ED6_DT27/CH03750 ._CH',             # 00
        'ED6_DT26/CH20445 ._CH',             # 01
        'ED6_DT26/CH20450 ._CH',             # 02
        'ED6_DT29/CH14540 ._CH',             # 03
        'ED6_DT29/CH14541 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03750P._CP',             # 00
        'ED6_DT26/CH20445P._CP',             # 01
        'ED6_DT26/CH20450P._CP',             # 02
        'ED6_DT29/CH14540P._CP',             # 03
        'ED6_DT29/CH14541P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -11870,
        Z                   = 0,
        Y                   = -4340,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = 0,
        Y                   = 4130,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16430,
        Z                   = 0,
        Y                   = 29760,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3250,
        Z                   = 0,
        Y                   = -18980,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 18540,
        Y                   = -1000,
        Z                   = -11640,
        Range               = 23800,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xF50,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -30480,
        Y                   = -1000,
        Z                   = -29590,
        Range               = -13210,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF969C,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -9850,
        TriggerZ            = 0,
        TriggerY            = 2640,
        TriggerRange        = 1000,
        ActorX              = -9850,
        ActorZ              = 1000,
        ActorY              = 2640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -25140,
        TriggerZ            = 0,
        TriggerY            = 4380,
        TriggerRange        = 1000,
        ActorX              = -25140,
        ActorZ              = 1000,
        ActorY              = 4380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27020,
        TriggerZ            = 0,
        TriggerY            = 4360,
        TriggerRange        = 1000,
        ActorX              = -27020,
        ActorZ              = 1000,
        ActorY              = 4360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4930,
        TriggerZ            = 0,
        TriggerY            = -18050,
        TriggerRange        = 1000,
        ActorX              = 4930,
        ActorZ              = 1000,
        ActorY              = -18050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24270,
        TriggerZ            = 0,
        TriggerY            = 15620,
        TriggerRange        = 1000,
        ActorX              = -24350,
        ActorZ              = 3000,
        ActorY              = 14740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_316",          # 00, 0
        "Function_1_32A",          # 01, 1
        "Function_2_3BC",          # 02, 2
        "Function_3_4E2",          # 03, 3
        "Function_4_608",          # 04, 4
        "Function_5_72E",          # 05, 5
        "Function_6_82E",          # 06, 6
        "Function_7_C63",          # 07, 7
        "Function_8_C74",          # 08, 8
        "Function_9_1603",         # 09, 9
        "Function_10_1640",        # 0A, 10
        "Function_11_165F",        # 0B, 11
        "Function_12_1683",        # 0C, 12
        "Function_13_16A7",        # 0D, 13
        "Function_14_16CB",        # 0E, 14
        "Function_15_16EF",        # 0F, 15
        "Function_16_1713",        # 10, 16
        "Function_17_1737",        # 11, 17
        "Function_18_175B",        # 12, 18
        "Function_19_177F",        # 13, 19
        "Function_20_2E8D",        # 14, 20
        "Function_21_2ED1",        # 15, 21
        "Function_22_2F45",        # 16, 22
        "Function_23_3110",        # 17, 23
        "Function_24_31C6",        # 18, 24
    )


    def Function_0_316(): pass

    label("Function_0_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_329")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_329")

    Return()

    # Function_0_316 end

    def Function_1_32A(): pass

    label("Function_1_32A")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x2300A2)
    OP_22(0x1CD, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353")
    OP_6F(0x2, 0)
    Jump("loc_35A")

    label("loc_353")

    OP_6F(0x2, 60)

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    OP_6F(0x3, 0)
    Jump("loc_373")

    label("loc_36C")

    OP_6F(0x3, 60)

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0x4, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0x4, 60)

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0x5, 0)
    Jump("loc_3A5")

    label("loc_39E")

    OP_6F(0x5, 60)

    label("loc_3A5")

    OP_82(0x94, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3B8")
    OP_82(0x95, 0x0)
    Jump("loc_3BB")

    label("loc_3B8")

    OP_82(0x96, 0x0)

    label("loc_3BB")

    Return()

    # Function_1_32A end

    def Function_2_3BC(): pass

    label("Function_2_3BC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_430")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    Jump("loc_415")

    label("loc_415")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B0)
    Jump("loc_49E")

    label("loc_430")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x02\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_47F")

    label("loc_47F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_49E")

    Jump("loc_4D4")

    label("loc_4A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3BC end

    def Function_3_4E2(): pass

    label("Function_3_4E2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2CB, 1)"), scpexpr(EXPR_END)), "loc_556")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xCB\x02\x07\x00。\x02",
    )

    Jump("loc_53B")

    label("loc_53B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B1)
    Jump("loc_5C4")

    label("loc_556")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xCB\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xCB\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5A5")

    label("loc_5A5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_5C4")

    Jump("loc_5FA")

    label("loc_5C7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5FA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4E2 end

    def Function_4_608(): pass

    label("Function_4_608")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4FD, 1)"), scpexpr(EXPR_END)), "loc_67C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFD\x04\x07\x00。\x02",
    )

    Jump("loc_661")

    label("loc_661")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B2)
    Jump("loc_6EA")

    label("loc_67C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFD\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6CB")

    label("loc_6CB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_6EA")

    Jump("loc_720")

    label("loc_6ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_720")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_608 end

    def Function_5_72E(): pass

    label("Function_5_72E")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)

    AnonymousTalk(    #9
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x29B3)
    Jump("loc_81C")

    label("loc_800")


    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_81C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_72E end

    def Function_6_82E(): pass

    label("Function_6_82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_END)), "loc_836")
    Return()

    label("loc_836")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFA")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 13600, 0, -1310, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Fade(500)
    OP_6C(225000, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #11
        0x10,
        "青年的声音",
        (
            "#1S不、不要啊……！#2S\x02\x03",

            "#1S你们别过来！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_989")

    label("loc_922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_989")

    label("loc_94A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_972")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_989")

    label("loc_972")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_989")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A1D")

    label("loc_9B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A1D")

    label("loc_9DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A06")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A1D")

    label("loc_A06")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A1D")

    Sleep(1000)

    def lambda_A28():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A28)
    Sleep(100)

    def lambda_A3B():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3B)
    Sleep(100)

    def lambda_A4E():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_A4E)
    Sleep(100)
    TurnDirection(0xF0, 0x10, 400)

    ChrTalk(    #12
        0x102,
        "#1504F#5P这个声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#5P啊啊……不会错的。\x02\x03",

            "#1840F声音是从对面传过来的，\x01",
            "还是先去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    OP_A2(0x2907)
    OP_28(0x33, 0x1, 0x4)
    Sleep(300)
    Jump("loc_C47")

    label("loc_AFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #14
        0x109,
        (
            "#1063F（总之，\x01",
            "  先到声音传过来的方向看看吧。）\x02\x03",

            "（离这里应该很近的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C47")

    label("loc_B64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BEF")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #15
        0x109,
        (
            "#1063F总之，\x01",
            "先到声音传过来的方向看看吧。\x02\x03",

            "离这里应该很近的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C47")

    label("loc_BEF")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #16
        0x109,
        (
            "#1063F总之，\x01",
            "先到声音传过来的方向看看吧。\x02\x03",

            "离这里应该很近的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C47")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_82E end

    def Function_7_C63(): pass

    label("Function_7_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_END)), "loc_C6B")
    Return()

    label("loc_C6B")

    Call(0, 8)
    Call(0, 19)
    Return()

    # Function_7_C63 end

    def Function_8_C74(): pass

    label("Function_8_C74")

    EventBegin(0x0)
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 42320, 1000, -6690, 270)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x12, 38210, 0, -5690, 90)
    SetChrPos(0x13, 39850, 0, -3470, 135)
    SetChrPos(0x14, 44470, 0, -4300, 225)
    SetChrPos(0x15, 43650, 0, -10050, 315)
    SetChrPos(0x16, 39470, 0, -9530, 0)

    def lambda_D47():

        label("loc_D47")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D47")

    QueueWorkItem2(0x12, 3, lambda_D47)

    def lambda_D5A():

        label("loc_D5A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D5A")

    QueueWorkItem2(0x13, 3, lambda_D5A)

    def lambda_D6D():

        label("loc_D6D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D6D")

    QueueWorkItem2(0x14, 3, lambda_D6D)

    def lambda_D80():

        label("loc_D80")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D80")

    QueueWorkItem2(0x15, 3, lambda_D80)

    def lambda_D93():

        label("loc_D93")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D93")

    QueueWorkItem2(0x16, 3, lambda_D93)
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 7)), scpexpr(EXPR_END)), "loc_DD2")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0x10, 400)
    Jump("loc_1087")

    label("loc_DD2")

    Fade(500)
    OP_6D(18700, 10, -6020, 0)
    OP_67(0, 8420, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0xEE, 18520, 0, -5690, 90)
    SetChrPos(0xEF, 18350, 0, -4260, 90)
    SetChrPos(0xF0, 17050, 0, -5550, 90)
    SetChrPos(0xF1, 16800, 0, -4000, 90)
    OP_0D()
    Sleep(300)

    NpcTalk(    #17
        0x10,
        "青年的声音",
        (
            "不、不要啊……！\x02\x03",

            "你们别过来！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F62")

    label("loc_EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F23")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F62")

    label("loc_F23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F62")

    label("loc_F4B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F62")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FF6")

    label("loc_F8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FF6")

    label("loc_FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FF6")

    label("loc_FDF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FF6")

    Sleep(500)

    def lambda_1001():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1001)
    Sleep(50)

    def lambda_1014():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1014)
    Sleep(50)

    def lambda_1027():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1027)
    Sleep(50)
    TurnDirection(0x3, 0x10, 400)

    ChrTalk(    #18
        0x102,
        "#1504F#6P这个声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1063F#5P啊啊……不会错的。\x02",
    )

    CloseMessageWindow()

    label("loc_1087")


    def lambda_108D():
        OP_6D(43350, 0, -6810, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_108D)

    def lambda_10A5():
        OP_67(0, 6670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10A5)

    def lambda_10BD():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10BD)

    def lambda_10CD():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10CD)

    def lambda_10DD():
        OP_6E(255, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10DD)
    Sleep(2500)
    OP_1D(0xB4)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x109, 33500, 0, -4180, 90)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0x9)
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#1224F只、只是我一时冲动罢了！\x02\x03",

            "不会再有第二次了！\x01",
            "求、求你们饶我一命啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)

    def lambda_11B7():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11B7)
    OP_43(0x12, 0x0, 0x0, 0xA)
    OP_43(0x13, 0x0, 0x0, 0xB)
    OP_43(0x14, 0x0, 0x0, 0xC)
    OP_43(0x15, 0x0, 0x0, 0xD)
    OP_43(0x16, 0x0, 0x0, 0xE)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #21
        0x109,
        (
            "#5P唉……\x01",
            "真是莫名其妙的缘分啊。\x02",
        )
    )

    Jump("loc_123C")

    label("loc_123C")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x10, 0x0)
    SetChrPos(0xEE, 25640, 670, -5350, 90)
    SetChrPos(0xEF, 25090, 60, -4120, 90)
    SetChrPos(0xF0, 23470, 500, -5000, 90)
    SetChrPos(0xF1, 22490, 0, -3200, 90)
    Fade(500)
    ClearMapFlags(0x10)
    SetChrPos(0x10, 42400, 900, -6550, 270)
    OP_6D(39000, 550, -7300, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(143000, 0)
    OP_6E(288, 0)
    OP_43(0x109, 0x0, 0x0, 0xF)
    OP_43(0x102, 0x0, 0x0, 0x10)
    OP_43(0xF0, 0x0, 0x0, 0x11)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Sleep(500)

    def lambda_1320():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1320)
    Sleep(50)

    def lambda_1333():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1333)
    Sleep(50)

    def lambda_1346():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1346)
    Sleep(50)

    def lambda_1359():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1359)
    Sleep(50)
    OP_8C(0x16, 270, 400)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        (
            "#1225F#5P哦哦哦！？\x01",
            "这、这一定是女神的指引！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #23
        0x10,
        (
            "#1227F#3S#5P神父大人！　约修亚大人！\x01",
            "求你们救救我吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1512F#5P……没办法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1840F#11P要是见死不救，良心上也过不去，\x01",
            "还是去帮他吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1493():
        OP_6D(36580, 0, -7280, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1493)

    def lambda_14AB():
        OP_67(0, 8350, -10000, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14AB)

    def lambda_14C3():
        OP_6B(2660, 400)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14C3)

    def lambda_14D3():
        OP_6E(266, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_14D3)
    SetChrChipByIndex(0x12, 4)

    def lambda_14E8():

        label("loc_14E8")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_14E8")

    QueueWorkItem2(0x12, 3, lambda_14E8)

    def lambda_14FB():
        OP_8F(0xFE, 0x899E, 0x0, 0xFFFFE930, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_14FB)
    Sleep(10)
    SetChrChipByIndex(0x15, 4)

    def lambda_1520():

        label("loc_1520")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1520")

    QueueWorkItem2(0x15, 3, lambda_1520)

    def lambda_1533():
        OP_8F(0xFE, 0x88A4, 0x0, 0xFFFFE638, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1533)
    Sleep(15)
    SetChrChipByIndex(0x13, 4)

    def lambda_1558():

        label("loc_1558")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1558")

    QueueWorkItem2(0x13, 3, lambda_1558)

    def lambda_156B():
        OP_8F(0xFE, 0x8B24, 0x0, 0xFFFFEB88, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_156B)
    Sleep(10)
    SetChrChipByIndex(0x14, 4)

    def lambda_1590():

        label("loc_1590")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1590")

    QueueWorkItem2(0x14, 3, lambda_1590)

    def lambda_15A3():
        OP_8F(0xFE, 0x899E, 0x0, 0xFFFFE930, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_15A3)
    Sleep(15)
    SetChrChipByIndex(0x16, 4)

    def lambda_15C8():

        label("loc_15C8")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_15C8")

    QueueWorkItem2(0x16, 3, lambda_15C8)

    def lambda_15DB():
        OP_8F(0xFE, 0x88AE, 0x0, 0xFFFFE3FE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_15DB)
    WaitChrThread(0x109, 0x0)
    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_C74 end

    def Function_9_1603(): pass

    label("Function_9_1603")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_9_1603")

    label("loc_163F")

    Return()

    # Function_9_1603 end

    def Function_10_1640(): pass

    label("Function_10_1640")

    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0x9C9A, 0x0, 0xFFFFE7DC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_10_1640 end

    def Function_11_165F(): pass

    label("Function_11_165F")

    Sleep(100)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA096, 0x0, 0xFFFFEC8C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_11_165F end

    def Function_12_1683(): pass

    label("Function_12_1683")

    Sleep(120)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA8B6, 0x0, 0xFFFFEB74, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_12_1683 end

    def Function_13_16A7(): pass

    label("Function_13_16A7")

    Sleep(30)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA7BC, 0x0, 0xFFFFDEB8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_13_16A7 end

    def Function_14_16CB(): pass

    label("Function_14_16CB")

    Sleep(60)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0x9F1A, 0x0, 0xFFFFE099, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_14_16CB end

    def Function_15_16EF(): pass

    label("Function_15_16EF")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x8426, 0x0, 0xFFFFE5FC, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_16EF end

    def Function_16_1713(): pass

    label("Function_16_1713")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x844E, 0x0, 0xFFFFEBB0, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_16_1713 end

    def Function_17_1737(): pass

    label("Function_17_1737")

    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x7E36, 0x0, 0xFFFFE638, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_17_1737 end

    def Function_18_175B(): pass

    label("Function_18_175B")

    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x7DFA, 0x0, 0xFFFFEC8C, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_18_175B end

    def Function_19_177F(): pass

    label("Function_19_177F")

    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    SetChrPos(0xEE, 37940, 0, -6610, 90)
    SetChrPos(0xEF, 38210, 0, -5250, 90)
    SetChrPos(0xF0, 36330, 0, -6400, 90)
    SetChrPos(0xF1, 36670, 0, -4740, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 40920, 0, -6220, 270)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 40560, 0, -6340, 270)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(39860, 0, -6820, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(135000, 0)
    OP_6E(292, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#1228F#5P呼、呼、呼……\x02\x03",

            "真、真是过分啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1068F#12P唉……\x01",
            "小哥你也算是结社的人吧？\x02\x03",

            "#1063F怎么每次\x01",
            "都碰上这种事啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrSubChip(0x10, 1)
    OP_0D()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #28
        0x10,
        (
            "#1222F#5P真、真没礼貌……\x02\x03",

            "这要说起来\x01",
            "可是催人泪下波澜万丈\x01",
            "惊天动地的故事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1505F#6P这你就别说了……\x01",
            "我倒是有个直接的疑问。\x02\x03",

            "#1502F为什么你会比我们\x01",
            "先到这个地方来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1079F#12P难道是比我们\x01",
            "先进入了传送阵？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1220F#5P呼，在王城里和你们分别后，\x01",
            "我就在街上被甲胄兵围起来了。\x02\x03",

            "#1226F就在我奋勇杀敌\x01",
            "打倒逼进的甲胄兵时，\x01",
            "突然被漩涡一样的东西卷了进去。\x02\x03",

            "等我清醒过来，发现已经来到了\x01",
            "一座能看到壮丽绝景的建筑物前。\x02\x03",

            "#1221F哦哦，这真是奇迹！\x01",
            "女神一定是把我基尔巴特·斯坦因\x01",
            "选为故事的主人公了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFD")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C64")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C25")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C64")

    label("loc_1C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4D")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1C64")

    label("loc_1C4D")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1C64")

    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA8")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D0F")

    label("loc_1CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD0")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D0F")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF8")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1D0F")

    label("loc_1CF8")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1D0F")

    Sleep(1500)

    ChrTalk(    #32
        0x102,
        "#1508F#6P（凯文先生，这是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1068F#11P（啊啊，是被战斗中偶然发生的\x01",
            "  『漩涡』给卷进来了吧……）\x02\x03",

            "#1840F（不过他居然巧合地\x01",
            "  飞到『第四星层』……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(    #34
        0x10B,
        (
            "#413F#12P（唉……\x01",
            "  这运气也真是差到家了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1E14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6A")

    ChrTalk(    #35
        0x10A,
        (
            "#819F#12P（啊哈哈……\x01",
            "  到底算是运气好还是运气差呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB5")

    ChrTalk(    #36
        0x104,
        (
            "#1541F#12P（呼……\x01",
            "  这运气也真是差到家了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F03")

    ChrTalk(    #37
        0x108,
        (
            "#573F#12P（哎呀哎呀……\x01",
            "  这噩运可真了不得啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F56")

    ChrTalk(    #38
        0x105,
        (
            "#1165F#12P（嗯……\x01",
            "  到底算是运气好还是运气差呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1F56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAA")

    ChrTalk(    #39
        0x10D,
        (
            "#278F#12P（哼……\x01",
            "  你也只有噩运才能让人甘拜下风啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFB")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(    #40
        0x10E,
        (
            "#179F#12P（呼……\x01",
            "  你也只有噩运才能让人甘拜下风啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFB")


    ChrTalk(    #41
        0x10,
        (
            "#1221F#5P呼，\x01",
            "感动得连话也说不出来了吗。\x02\x03",

            "#1226F呵呵……这也难怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1068F#12P嗯，\x01",
            "在某种其它的意义上确实有所感动……\x02\x03",

            "#1060F那么，你又为什么\x01",
            "离开宿舍来到这种地方？\x02\x03",

            "也是在探索吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #43
        0x10,
        "#1224F#5P（惊慌）……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1504F#6P这么说来……\x02\x03",

            "你刚才说什么『不会再有第二次了』、\x01",
            "『一时冲动』之类的，\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1226F#5P哈、哈哈……\x01",
            "你～在说～什～么～呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2211")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2269")

    label("loc_2211")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2234")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2269")

    label("loc_2234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2257")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2269")

    label("loc_2257")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228C")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_22E4")

    label("loc_228C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AF")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_22E4")

    label("loc_22AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D2")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_22E4")

    label("loc_22D2")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_22E4")

    Sleep(2000)
    OP_63(0x109)
    OP_63(0x102)
    OP_63(0xF0)
    OP_63(0xF1)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #46
        0x10,
        (
            "#1224F#5P不、不是的！\x02\x03",

            "那是……\x01",
            "那只是慌张的时候说胡话……\x02",
        )
    )

    Jump("loc_2365")

    label("loc_2365")

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1841F#12P……难不成……\x02\x03",

            "#1840F你肚子太饿，\x01",
            "跑到刚才那些兽人那里\x01",
            "偷它们的食物了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#1224F#5P（更加惊慌）……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2444")

    ChrTalk(    #49
        0x107,
        (
            "#069F#12P好、好可怜……\x02\x03",

            "竟然被逼到\x01",
            "这种地步……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B4")

    ChrTalk(    #50
        0x105,
        (
            "#1382F#12P嗯，那个……\x01",
            "我觉得没什么好害臊的。\x02\x03",

            "#1165F吃饱肚子是很重要的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2522")

    label("loc_24B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2522")

    ChrTalk(    #51
        0x104,
        (
            "#1541F#12P呼……\x01",
            "没什么好害臊的。\x02\x03",

            "#1540F衣食足而知礼节──\x01",
            "话不都这么说吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A0")

    ChrTalk(    #52
        0x10B,
        (
            "#413F#12P唉，虽然不是不值得同情……\x02\x03",

            "#210F但因此做了多余的事\x01",
            "被魔物抓起来可就真是没救了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2613")

    label("loc_25A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2613")

    ChrTalk(    #53
        0x10E,
        (
            "#176F#12P呼，虽然值得同情……\x02\x03",

            "#178F但因此做了多余的事\x01",
            "招致危机可就本末倒置了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2659")

    ChrTalk(    #54
        0x108,
        (
            "#075F#12P哎呀哎呀……\x01",
            "做这么危险的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2696")

    label("loc_2659")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2696")

    ChrTalk(    #55
        0x10D,
        (
            "#272F#12P哼……\x01",
            "这就叫自作自受啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(    #56
        0x10A,
        (
            "#1317F#12P那、那个……\x02\x03",

            "#819F要不要吃点饼干？\x01",
            "我带来当零食的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F8")


    ChrTalk(    #57
        0x102,
        (
            "#1505F#6P……基尔巴特。\x02\x03",

            "#1514F那个，不介意的话\x01",
            "来我们的『据点』可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1840F#12P是啊……\x02\x03",

            "到那里的话\x01",
            "水和食物都有保证。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        (
            "#1227F#5P喂、喂！\x01",
            "别用这种怜悯的目光看我！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0xA3, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_2810():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFE778, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2810)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(300)

    ChrTalk(    #60
        0x10,
        (
            "#1225F#5P真不凑巧，\x01",
            "食物我才从刚才那些家伙那里偷到！\x02\x03",

            "而且还是足够\x01",
            "过一个月的量呢！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_28AA():
        OP_6D(33590, 0, -6230, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28AA)

    def lambda_28C2():
        OP_67(0, 7700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_28C2)

    def lambda_28DA():
        OP_6B(3050, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_28DA)

    def lambda_28EA():
        OP_6C(225000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28EA)

    def lambda_28FA():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28FA)
    OP_43(0x10, 0x0, 0x0, 0x14)

    def lambda_2911():

        label("loc_2911")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2911")

    QueueWorkItem2(0x109, 0, lambda_2911)

    def lambda_2922():

        label("loc_2922")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2922")

    QueueWorkItem2(0x102, 0, lambda_2922)

    def lambda_2933():

        label("loc_2933")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2933")

    QueueWorkItem2(0xF0, 0, lambda_2933)

    def lambda_2944():

        label("loc_2944")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2944")

    QueueWorkItem2(0xF1, 0, lambda_2944)
    Sleep(3000)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)

    def lambda_296A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_296A)

    def lambda_2978():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2978)

    def lambda_2986():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2986)

    def lambda_2994():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2994)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #61
        0x10,
        (
            "#1221F#11P哼，这些食物\x01",
            "全是我一个人的！\x02\x03",

            "连剩渣都不会\x01",
            "分给你们的！\x02\x03",

            "#1226F哈哈，那就再见了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    def lambda_2A2A():
        OP_6D(31450, 0, -6180, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A2A)

    def lambda_2A42():
        OP_8E(0xFE, 0x1C02, 0x0, 0xFFFFF16E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2A42)
    WaitChrThread(0x109, 0x0)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9B")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2B02")

    label("loc_2A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC3")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2B02")

    label("loc_2AC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEB")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2B02")

    label("loc_2AEB")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2B02")

    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B46")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2BAD")

    label("loc_2B46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6E")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2BAD")

    label("loc_2B6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B96")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2BAD")

    label("loc_2B96")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2BAD")

    Sleep(1500)

    def lambda_2BB8():
        OP_6D(35750, 0, -7170, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2BB8)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1068F#5P唉……\x01",
            "这小哥真是不听劝啊。\x02\x03",

            "#1840F话说回来，\x01",
            "难道他打算在这种地方待一个月吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1505F#6P唉，现在就别理他了吧。\x02\x03",

            "#1500F大概他很快又会\x01",
            "大吵大闹地来求我们了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CD5")

    ChrTalk(    #64
        0x107,
        "#067F#5P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D09")

    ChrTalk(    #65
        0x10E,
        "#179F#5P呵呵……的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2D09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3F")

    ChrTalk(    #66
        0x10D,
        "#278F#5P呼……的确是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D7B")

    ChrTalk(    #67
        0x105,
        (
            "#1165F#5P呵呵……\x01",
            "很有可能呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2D7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB3")

    ChrTalk(    #68
        0x108,
        "#070F#5P呵呵……的确是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DEF")

    ChrTalk(    #69
        0x104,
        (
            "#1541F#5P呼……\x01",
            "很有这可能呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(    #70
        0x10A,
        (
            "#819F#5P啊哈哈……\x01",
            "说不定真是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2F")


    ChrTalk(    #71
        0x109,
        (
            "#1066F#5P哈哈，\x01",
            "到时候再好好热烈欢迎他吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2908)
    OP_28(0x33, 0x1, 0x8)
    OP_28(0x33, 0x1, 0x10)
    OP_28(0x33, 0x1, 0x20)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_19_177F end

    def Function_20_2E8D(): pass

    label("Function_20_2E8D")

    OP_8E(0xFE, 0x9D62, 0x0, 0xFFFFDDA0, 0x1B58, 0x0)
    OP_8E(0xFE, 0x8868, 0x0, 0xFFFFDD96, 0x1B58, 0x0)
    OP_8E(0xFE, 0x7B20, 0x0, 0xFFFFEDF4, 0x1B58, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_20_2E8D end

    def Function_21_2ED1(): pass

    label("Function_21_2ED1")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_2F2E")

    label("loc_2F2E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_21_2ED1 end

    def Function_22_2F45(): pass

    label("Function_22_2F45")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -25530, 0, 17040, 180)
    SetChrPos(0x1, -23780, 0, 17410, 180)
    SetChrPos(0x2, -25750, 0, 18940, 180)
    SetChrPos(0x3, -23820, 0, 19550, 180)
    OP_6D(-24210, 0, 16120, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(4310, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301B")
    OP_28(0x3, 0x4, 0x2)
    OP_82(0x95, 0x2)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_301B")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #73
        (
            "\x07\x05#40W　　汝须将旭日般辉耀之少女\x01",
            " 与支持陪伴此光辉之少年一同\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3104")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3101")
    Call(0, 23)

    label("loc_3101")

    Jump("loc_3104")

    label("loc_3104")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_22_2F45 end

    def Function_23_3110(): pass

    label("Function_23_3110")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)

    def lambda_3179():
        OP_6B(3930, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3179)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x11, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3110 end

    def Function_24_31C6(): pass

    label("Function_24_31C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -25530, 0, 17040, 180)
    SetChrPos(0x1, -23780, 0, 17410, 180)
    SetChrPos(0x2, -25750, 0, 18940, 180)
    SetChrPos(0x3, -23820, 0, 19550, 180)
    OP_6D(-24210, 0, 16120, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(4310, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_24_31C6 end

    SaveToFile()

Try(main)
