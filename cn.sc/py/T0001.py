from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001   ._SN',
        MapName             = 'map1',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 16,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0001   ._SN',
            'ED6_DT21/T0001_1 ._SN',
            'ED6_DT21/T0001_2 ._SN',
            'ED6_DT21/T0001_3 ._SN',
            'ED6_DT21/T0001_4 ._SN',
            'ED6_DT21/T0001_5 ._SN',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '居民１',                               # 9
        '呜喵',                                 # 10
        '宝箱',                                 # 11
        '宝箱',                                 # 12
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH10000 ._CH',             # 01
        'ED6_DT09/CH10001 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH10000P._CP',             # 01
        'ED6_DT09/CH10001P._CP',             # 02
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10000,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 10000,
        Y                   = 0,
        Z                   = -1000,
        Range               = 11000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 2000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C6",          # 00, 0
        "Function_1_1C7",          # 01, 1
        "Function_2_387",          # 02, 2
        "Function_3_390",          # 03, 3
        "Function_4_391",          # 04, 4
        "Function_5_396",          # 05, 5
        "Function_6_643",          # 06, 6
        "Function_7_668",          # 07, 7
        "Function_8_6A4",          # 08, 8
        "Function_9_6B9",          # 09, 9
        "Function_10_6DD",         # 0A, 10
        "Function_11_7A7",         # 0B, 11
        "Function_12_1011",        # 0C, 12
        "Function_13_115B",        # 0D, 13
        "Function_14_11D7",        # 0E, 14
        "Function_15_11E5",        # 0F, 15
        "Function_16_11EF",        # 10, 16
        "Function_17_1257",        # 11, 17
        "Function_18_1266",        # 12, 18
        "Function_19_1337",        # 13, 19
        "Function_20_1352",        # 14, 20
        "Function_21_136D",        # 15, 21
        "Function_22_1386",        # 16, 22
        "Function_23_13AC",        # 17, 23
    )


    def Function_0_1C6(): pass

    label("Function_0_1C6")

    Return()

    # Function_0_1C6 end

    def Function_1_1C7(): pass

    label("Function_1_1C7")

    Event(0, 11)
    OP_62(0x9, 0xFFFFFDA8, 300, 0x80, 0x21, 0xFA, 0x0)
    SetChrFlags(0x9, 0x6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -4000, 1000, -2000, 0)
    OP_51(0x9, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377")
    OP_A2(0x1000)
    RemoveParty(0x0, 0xFF)
    AddParty(0x1, 0xF6, 0x0)
    AddParty(0x0, 0xF7, 0x1)
    AddParty(0x5, 0xF8, 0x2)
    AddParty(0x6, 0xF9, 0x3)
    Call(2, 58)
    OP_31(0x0, 0x7, 0x4)
    OP_31(0x0, 0x0, 0x3)
    OP_31(0x1, 0x7, 0x3)
    OP_31(0x0, 0x7, 0x3)
    OP_35(0x0, 0x96)
    OP_35(0x0, 0x97)
    OP_35(0x0, 0x98)
    OP_35(0x0, 0x99)
    OP_35(0x0, 0x9A)
    OP_35(0x1, 0xA0)
    OP_35(0x1, 0xA1)
    OP_35(0x1, 0xA4)
    OP_35(0x1, 0xA2)
    OP_35(0x1, 0xA3)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_35(0x3, 0xB6)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDC)
    OP_35(0x0, 0x8C)
    OP_35(0x1, 0x8C)
    OP_35(0x2, 0x8C)
    OP_35(0x3, 0x8C)
    OP_35(0x4, 0x8C)
    OP_35(0x5, 0x8C)
    OP_35(0x6, 0x8C)
    OP_35(0x7, 0x8C)
    OP_36(0x0, 0xE6)
    OP_36(0x0, 0xE7)
    OP_36(0x0, 0xE8)
    OP_36(0x1, 0xEB)
    OP_36(0x1, 0xEC)
    OP_36(0x1, 0xED)
    OP_36(0x2, 0xF0)
    OP_36(0x2, 0xF1)
    OP_36(0x3, 0xF5)
    OP_36(0x3, 0xF6)
    OP_36(0x4, 0xFA)
    OP_36(0x4, 0xFB)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_36(0x5, 0x101)
    OP_36(0x6, 0x104)
    OP_36(0x6, 0x105)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    OP_36(0x7, 0x10B)
    OP_36(0xA, 0x112)
    OP_35(0x8, 0x82)
    OP_36(0x8, 0x10E)
    OP_3E(0x258, 1)
    OP_3E(0x259, 1)
    OP_3E(0x25E, 1)
    OP_3E(0x1F5, 50)
    SetMapFlags(0x1000000)

    label("loc_377")

    SetMapFlags(0x1)
    ClearMapFlags(0x20)
    ClearMapFlags(0x400000)
    Return()

    # Function_1_1C7 end

    def Function_2_387(): pass

    label("Function_2_387")

    OP_D7(0x1, 50000, 0)
    Return()

    # Function_2_387 end

    def Function_3_390(): pass

    label("Function_3_390")

    Return()

    # Function_3_390 end

    def Function_4_391(): pass

    label("Function_4_391")

    Call(0, 11)
    Return()

    # Function_4_391 end

    def Function_5_396(): pass

    label("Function_5_396")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3B6")

    ChrTalk(    #0
        0xFE,
        "立着地点标旗哦～\x02",
    )

    CloseMessageWindow()

    label("loc_3B6")

    OP_A2(0x12)
    SetMessageWindowPos(100, 100, 15, 2)

    AnonymousTalk(    #1
        (
            "#200W可以指定坐标显示哦。\x02\x01",

            "#W真的哦\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2 op#A
        (
            "#20A2等两秒～\x02",

            "#A如果不指定坐标，\x01",
            "画面中央是中心圆（center ring）～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        "请指定恢复时的默认坐标。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #4
        0xFE,
        "#010F#1P停止左上\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#010F#2P停止右上\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#010F#3P停止左下\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#010F#4P停止右下\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#010F#5P停止直上\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#010F#6P停止直下\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "只要按下F11，就能看见\x01",
            "任务区域等地，明白了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#010F我要，和爱娜！白头偕老！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x1,
        "#020F哦哦？哈～哈、哈、哈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1,
        (
            "#020F没想到会在这种地方\x01",
            "遇见爱娜小姐的心上人。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("约修亚")

    AnonymousTalk(    #14
        (
            "#000F暑假已经结束了。\x02\x01",

            "#4S啊啊啊啊啊\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    AnonymousTalk(    #15
        (
            "#F#2Sあいうえお#10R a   i   u   e   o#\x02\x01",

            "かきくけこ#10R ka  ki  ku  ke  ko#さしすせそ#10R sa  si  su  se  so#\x01",
            "真是的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_396 end

    def Function_6_643(): pass

    label("Function_6_643")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_667")
    OP_8D(0xFE, 5000, -5000, 15000, 9000, 2000)
    OP_48()
    Jump("Function_6_643")

    label("loc_667")

    Return()

    # Function_6_643 end

    def Function_7_668(): pass

    label("Function_7_668")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A3")
    OP_70(0x1, 0x32)
    OP_8D(0xFE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x8)
    Sleep(2000)
    Jump("Function_7_668")

    label("loc_6A3")

    Return()

    # Function_7_668 end

    def Function_8_6A4(): pass

    label("Function_8_6A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B8")
    OP_8C(0xFE, 180, 5000)
    OP_48()
    Jump("Function_8_6A4")

    label("loc_6B8")

    Return()

    # Function_8_6A4 end

    def Function_9_6B9(): pass

    label("Function_9_6B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DC")
    OP_8D(0x0, 10000, 10000, -10000, -10000, 2000)
    Jump("Function_9_6B9")

    label("loc_6DC")

    Return()

    # Function_9_6B9 end

    def Function_10_6DD(): pass

    label("Function_10_6DD")

    OP_A1(0xA, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x100)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x2710, 0x7D0, 0x2710)
    OP_98(0x1, 0x1388, 0x1770, 0x4E20)

    def lambda_723():
        OP_98(0x2, 0xA, 0x7D0, 0x6)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_723)
    WaitChrThread(0xA, 0x2)
    OP_8E(0xA, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x1B58, 0x0, 0x1388)
    OP_98(0x1, 0x2710, 0x7D0, 0x1F40)
    OP_98(0x1, 0x3A98, 0x1388, 0x1B58)
    OP_98(0x2, 0xA, 0x7D0, 0x2)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x2710, 0xFFFFEC78, 0x7D0)
    OP_98(0x1, 0x2710, 0x2710, 0xFFFFEC78)
    OP_98(0x2, 0xA, 0x7D0, 0x2)
    Return()

    # Function_10_6DD end

    def Function_11_7A7(): pass

    label("Function_11_7A7")

    OP_16(0x1)
    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #16
        "取得号\x02",
    )

    OP_57(0x0, 0x0, 0x12, "#1C菜单标题")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1003")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "测试地图\x01",                  # 0
            "游戏地图\x01",                  # 1
            "角色一览\x01",                  # 2
            "魔兽一览\x01",                  # 3
            "战斗\x01",                      # 4
            "战斗（魔兽算法测试）\x01",      # 5
            "战斗（地图确认）\x01",          # 6
            "迷你游戏\x01",                  # 7
            "事件列表\x01",                  # 8
            "商店测试\x01",                  # 9
            "前篇后编角色替换新画\x01",      # 10
            "*Trap Land\x01",                # 11
            "头像\x01",                      # 12
            "组队选择菜单\x01",              # 13
            "*模糊（blur）\x01",             # 14
            "道具菜单\x01",                  # 15
            "*出不来！存档菜单\x01",         # 16
            "手册标志树立完毕\x01",          # 17
            "菜谱收集完整\x01",              # 18
            "游戏通关\x01",                  # 19
            "Camp菜单\x01",                  # 20
            "动画播放·停止\x01",            # 21
            "取消\x01",                      # 22
        )
    )

    MenuEnd(0x0)
    OP_16(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_95F"),
        (1, "loc_966"),
        (2, "loc_96D"),
        (3, "loc_974"),
        (4, "loc_97B"),
        (5, "loc_982"),
        (6, "loc_989"),
        (7, "loc_990"),
        (8, "loc_997"),
        (9, "loc_9A1"),
        (10, "loc_9AD"),
        (11, "loc_A5B"),
        (12, "loc_A67"),
        (13, "loc_C66"),
        (14, "loc_D00"),
        (15, "loc_D3B"),
        (16, "loc_D42"),
        (17, "loc_D46"),
        (18, "loc_D4D"),
        (19, "loc_D54"),
        (20, "loc_D70"),
        (21, "loc_FC6"),
        (SWITCH_DEFAULT, "loc_FF3"),
    )


    label("loc_95F")

    Call(0, 12)
    Jump("loc_1000")

    label("loc_966")

    Call(3, 6)
    Jump("loc_1000")

    label("loc_96D")

    Call(3, 0)
    Jump("loc_1000")

    label("loc_974")

    Call(3, 3)
    Jump("loc_1000")

    label("loc_97B")

    Call(2, 0)
    Jump("loc_1000")

    label("loc_982")

    Call(1, 0)
    Jump("loc_1000")

    label("loc_989")

    Call(2, 1)
    Jump("loc_1000")

    label("loc_990")

    Call(2, 59)
    Jump("loc_1000")

    label("loc_997")

    OP_66(0x1)
    Call(4, 0)
    Jump("loc_1000")

    label("loc_9A1")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 18)
    Jump("loc_1000")

    label("loc_9AD")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "艾丝蒂尔后篇，约修亚后篇\x01",      # 0
            "艾丝蒂尔前篇，约修亚前篇\x01",      # 1
            "约修亚后半，科洛丝后半\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A17"),
        (1, "loc_A28"),
        (2, "loc_A39"),
        (SWITCH_DEFAULT, "loc_A4A"),
    )


    label("loc_A17")

    OP_BB(0x0, 0x1, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    Jump("loc_A4A")

    label("loc_A28")

    OP_BB(0x0, 0x1, 0x1E)
    OP_BB(0x1, 0x1, 0x1F)
    Jump("loc_A4A")

    label("loc_A39")

    OP_BB(0x4, 0x1, 0x1D)
    OP_BB(0x1, 0x1, 0x1C)
    Jump("loc_A4A")

    label("loc_A4A")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_BD()
    Jump("loc_1000")

    label("loc_A5B")

    NewScene("ED6_DT21/A0019   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1000")

    label("loc_A67")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(1000)
    OP_D9(0x0, "CTI00110")
    Sleep(2000)
    OP_D9(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x1FF, 0x1FF, 0xFFFFFF, 0x0, "C_VIS000._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x1, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x154, 0xFA, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS001._CH")
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x0, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x168, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x2, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x17C, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x3, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x190, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x3, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x0, 0, 0, 1000)
    OP_C6(0x0, 0x2, 90000, 2000, 0)
    OP_C7(0x0, 0x0, 0x0)

    AnonymousTalk(    #17
        "噢\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x0, 360000, 260000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x1, 0, 1000, 1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    OP_C6(0x3, 0x1, 10000, 0, 500)
    OP_C7(0x0, 0xFF, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Jump("loc_1000")

    label("loc_C66")

    OP_5F(0x0)
    OP_56(0x0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xFFFF)

    ChrTalk(    #18
        0xF8,
        "Ｏｋ\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD")

    ChrTalk(    #19
        0xF7,
        "队友１科洛丝\x02",
    )

    Jump("loc_CFC")

    label("loc_CBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")

    ChrTalk(    #20
        0xF7,
        "队友１约修亚\x02",
    )

    Jump("loc_CFC")

    label("loc_CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFC")

    ChrTalk(    #21
        0xF7,
        "队友１阿加特\x02",
    )


    label("loc_CFC")

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_D00")

    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    ChrTalk(    #22
        0xF6,
        "*模糊（blur）\x02",
    )

    Sleep(2000)
    OP_15(0x1F4)

    ChrTalk(    #23
        0xF6,
        "那么\x02",
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_D3B")

    OP_18()
    ExitThread()
    ExitThread()
    ExitThread()
    Jump("loc_1000")

    label("loc_D42")

    ShowSaveMenu()
    Jump("loc_1000")

    label("loc_D46")

    Call(5, 0)
    Jump("loc_1000")

    label("loc_D4D")

    Call(5, 1)
    Jump("loc_1000")

    label("loc_D54")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22AE)
    FadeToDark(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x1)
    Jump("loc_1000")

    label("loc_D70")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_A3(0x16)

    label("loc_D7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB0")
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #24
        (
            "\x06\x18\x07\x05※进行队伍的重新编组。\x01",
            "　更换队员，进行必要的装备变更，\x01",
            "　确定后，请选择【继续】。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【编成队伍】\x01",      # 0
            "【变更装备】\x01",      # 1
            "【继续】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA5")
    OP_A2(0x16)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_FAD")

    label("loc_EA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_EDE")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_F0D")

    label("loc_EDE")


    AnonymousTalk(    #26
        "\x07\x05※请在进行队伍的编组之后再选择。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_F0D")

    Jump("loc_FAD")

    label("loc_F10")

    SetChrName("")

    AnonymousTalk(    #27
        "\x06\x18\x07\x05可以继续事件剧情了吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F91")
    SetChrName("")

    AnonymousTalk(    #28
        "\x06\x18\x07\x05继续事件发展。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_FB0")

    label("loc_F91")

    SetChrName("")

    AnonymousTalk(    #29
        "\x06\x18\x07\x05返回选择画面。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_FB0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(0, 0)
    OP_0D()
    Jump("loc_1000")

    label("loc_FAD")

    Jump("loc_D7A")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_FDA")
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_A3(0x15)
    Jump("loc_FF0")

    label("loc_FDA")

    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x0)
    OP_A2(0x15)

    label("loc_FF0")

    Jump("loc_1000")

    label("loc_FF3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1000")

    label("loc_1000")

    Jump("loc_7DA")

    label("loc_1003")

    OP_5F(0x0)
    OP_56(0x0)
    OP_DA()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_7A7 end

    def Function_12_1011(): pass

    label("Function_12_1011")


    AnonymousTalk(    #30
        "\x06请选择测试地图哦。\x02",
    )


    label("loc_1027")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114B")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试地图20\x01",      # 0
            "测试地图21\x01",      # 1
            "测试地图22\x01",      # 2
            "测试地图23\x01",      # 3
            "测试地图24\x01",      # 4
            "测试地图25\x01",      # 5
            "测试地图26\x01",      # 6
            "测试地图27\x01",      # 7
            "测试地图28\x01",      # 8
            "测试地图29\x01",      # 9
            "取消\x01",            # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10E4"),
        (1, "loc_10ED"),
        (2, "loc_10F6"),
        (3, "loc_10FF"),
        (4, "loc_1108"),
        (5, "loc_1111"),
        (6, "loc_111A"),
        (7, "loc_1123"),
        (8, "loc_112C"),
        (9, "loc_1135"),
        (SWITCH_DEFAULT, "loc_113E"),
    )


    label("loc_10E4")

    NewScene("ED6_DT21/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_10ED")

    NewScene("ED6_DT21/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_10F6")

    NewScene("ED6_DT21/T0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_10FF")

    NewScene("ED6_DT21/T0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1108")

    NewScene("ED6_DT21/T0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1111")

    NewScene("ED6_DT21/T0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_111A")

    NewScene("ED6_DT21/T0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1123")

    NewScene("ED6_DT21/T0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_112C")

    NewScene("ED6_DT21/T0028   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1135")

    NewScene("ED6_DT21/T0029   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_113E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1027")

    label("loc_114B")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1011 end

    def Function_13_115B(): pass

    label("Function_13_115B")


    AnonymousTalk(    #31
        "\x06哪个？\x02",
    )


    label("loc_1165")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C7")

    Menu(
        1,
        10,
        100,
        1,
        (
            "地图目标1\x01",      # 0
            "地图目标2\x01",      # 1
            "取消\x01",           # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11A8"),
        (1, "loc_11B1"),
        (SWITCH_DEFAULT, "loc_11BA"),
    )


    label("loc_11A8")

    NewScene("ED6_DT21/T0070   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11B1")

    NewScene("ED6_DT21/T0071   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_11BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1165")

    label("loc_11C7")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_115B end

    def Function_14_11D7(): pass

    label("Function_14_11D7")

    OP_6B(5000, 3000)
    Call(0, 15)
    Return()

    # Function_14_11D7 end

    def Function_15_11E5(): pass

    label("Function_15_11E5")

    OP_6C(0, 20000)
    Return()

    # Function_15_11E5 end

    def Function_16_11EF(): pass

    label("Function_16_11EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1238")
    EventBegin(0x0)
    OP_C2()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_1225")
    Sleep(1000)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_1233")

    label("loc_1225")


    AnonymousTalk(    #32
        "没有反应\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1233")

    EventEnd(0x0)
    Jump("loc_1256")

    label("loc_1238")


    AnonymousTalk(    #33
        "什么也没有发生(ByScript)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1256")

    Return()

    # Function_16_11EF end

    def Function_17_1257(): pass

    label("Function_17_1257")


    ChrTalk(    #34
        0x0,
        "欢迎\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_17_1257 end

    def Function_18_1266(): pass

    label("Function_18_1266")

    SetChrName("商店君")

    AnonymousTalk(    #35
        "\x06哪个店？\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "工房\x01",                      # 0
            "武器店\x01",                    # 1
            "道具店\x01",                    # 2
            "旅店\x01",                      # 3
            "协会\x01",                      # 4
            "读书（利贝尔通讯１）\x01",      # 5
            "娱乐场交换处\x01",              # 6
            "取消\x01",                      # 7
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12F7"),
        (1, "loc_12FE"),
        (2, "loc_1305"),
        (3, "loc_130C"),
        (4, "loc_1313"),
        (5, "loc_131A"),
        (6, "loc_1322"),
        (SWITCH_DEFAULT, "loc_1329"),
    )


    label("loc_12F7")

    Call(0, 17)
    Jump("loc_132C")

    label("loc_12FE")

    Call(0, 19)
    Jump("loc_132C")

    label("loc_1305")

    Call(0, 20)
    Jump("loc_132C")

    label("loc_130C")

    Call(0, 21)
    Jump("loc_132C")

    label("loc_1313")

    Call(0, 22)
    Jump("loc_132C")

    label("loc_131A")

    OP_B8(0x347, 0x0)
    Jump("loc_132C")

    label("loc_1322")

    Call(0, 23)
    Jump("loc_132C")

    label("loc_1329")

    Jump("loc_132C")

    label("loc_132C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_1266 end

    def Function_19_1337(): pass

    label("Function_19_1337")


    ChrTalk(    #36
        0x0,
        "欢迎光临武器店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_19_1337 end

    def Function_20_1352(): pass

    label("Function_20_1352")


    ChrTalk(    #37
        0x0,
        "欢迎光临道具店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x2)
    Return()

    # Function_20_1352 end

    def Function_21_136D(): pass

    label("Function_21_136D")


    ChrTalk(    #38
        0x0,
        "欢迎光临旅店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x5)
    Return()

    # Function_21_136D end

    def Function_22_1386(): pass

    label("Function_22_1386")


    ChrTalk(    #39
        0x0,
        "欢迎光临游击士协会！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x65, 0x66, 0x1, 0xFFFF)
    Return()

    # Function_22_1386 end

    def Function_23_13AC(): pass

    label("Function_23_13AC")


    ChrTalk(    #40
        0x0,
        "这里是交换所。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x69)
    Return()

    # Function_23_13AC end

    SaveToFile()

Try(main)
