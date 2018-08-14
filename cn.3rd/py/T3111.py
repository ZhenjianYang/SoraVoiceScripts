from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '丹',                                   # 9
        '阿加特',                               # 10
        '玛多克工房长',                         # 11
        '埃里克',                               # 12
        '海泽尔',                               # 13
        '菲',                                   # 14
        '奥克尔',                               # 15
        '目标用照相机',                         # 16
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
        'ED6_DT07/CH02030 ._CH',             # 00
        'ED6_DT27/CHDUMMY ._CH',             # 01
        'ED6_DT27/CHDUMMY ._CH',             # 02
        'ED6_DT29/CH14010 ._CH',             # 03
        'ED6_DT29/CH14131 ._CH',             # 04
        'ED6_DT29/CH14160 ._CH',             # 05
        'ED6_DT29/CH14190 ._CH',             # 06
        'ED6_DT29/CH14300 ._CH',             # 07
        'ED6_DT27/CH03980 ._CH',             # 08
        'ED6_DT06/CH20053 ._CH',             # 09
        'ED6_DT07/CH01450 ._CH',             # 0A
        'ED6_DT07/CH01540 ._CH',             # 0B
        'ED6_DT07/CH02620 ._CH',             # 0C
        'ED6_DT07/CH01550 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02030P._CP',             # 00
        'ED6_DT27/CHDUMMYP._CP',             # 01
        'ED6_DT27/CHDUMMYP._CP',             # 02
        'ED6_DT29/CH14010P._CP',             # 03
        'ED6_DT29/CH14131P._CP',             # 04
        'ED6_DT29/CH14160P._CP',             # 05
        'ED6_DT29/CH14190P._CP',             # 06
        'ED6_DT29/CH14300P._CP',             # 07
        'ED6_DT27/CH03980P._CP',             # 08
        'ED6_DT06/CH20053P._CP',             # 09
        'ED6_DT07/CH01450P._CP',             # 0A
        'ED6_DT07/CH01540P._CP',             # 0B
        'ED6_DT07/CH02620P._CP',             # 0C
        'ED6_DT07/CH01550P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8650,
        Z                   = 0,
        Y                   = -1430,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 6130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -111900,
        Z                   = -4000,
        Y                   = -111000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -110300,
        Z                   = -4000,
        Y                   = -111440,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 3900,
        TriggerRange        = 400,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 6130,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6900,
        TriggerZ            = 0,
        TriggerY            = -1410,
        TriggerRange        = 400,
        ActorX              = 8650,
        ActorZ              = 1500,
        ActorY              = -1430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -200120,
        TriggerZ            = 0,
        TriggerY            = 118010,
        TriggerRange        = 1200,
        ActorX              = -200120,
        ActorZ              = 1500,
        ActorY              = 118010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121030,
        TriggerZ            = -4000,
        TriggerY            = -99900,
        TriggerRange        = 800,
        ActorX              = -121030,
        ActorZ              = -3000,
        ActorY              = -99900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2F7",          # 01, 1
        "Function_2_38E",          # 02, 2
        "Function_3_3A4",          # 03, 3
        "Function_4_5C3",          # 04, 4
        "Function_5_719",          # 05, 5
        "Function_6_71E",          # 06, 6
        "Function_7_7FD",          # 07, 7
        "Function_8_802",          # 08, 8
        "Function_9_8C3",          # 09, 9
        "Function_10_116B",        # 0A, 10
        "Function_11_11CF",        # 0B, 11
        "Function_12_1227",        # 0C, 12
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    SetChrFlags(0x15, 0x10)

    label("loc_2D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2F6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_2F6")

    Return()

    # Function_0_2AA end

    def Function_1_2F7(): pass

    label("Function_1_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_333")
    OP_B1("T3111_1")
    OP_82(0x80, 0x0)
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()

    label("loc_333")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")
    OP_B1("T3111_1")
    OP_82(0x80, 0x0)
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()

    label("loc_36F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_37F"),
        (109, "loc_37F"),
        (SWITCH_DEFAULT, "loc_387"),
    )


    label("loc_37F")

    OP_22(0xA0, 0x1, 0x64)
    Jump("loc_38D")

    label("loc_387")

    OP_23(0xA0)
    Jump("loc_38D")

    label("loc_38D")

    Return()

    # Function_1_2F7 end

    def Function_2_38E(): pass

    label("Function_2_38E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_38E")

    label("loc_3A3")

    Return()

    # Function_2_38E end

    def Function_3_3A4(): pass

    label("Function_3_3A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 4)), scpexpr(EXPR_END)), "loc_4AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_415")

    ChrTalk(    #0
        0xFE,
        (
            "我正在把后续工作\x01",
            "交待给奥克尔先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "嗯，\x01",
            "这里的工作是有点诀窍的。\x02",
        )
    )

    Jump("loc_411")

    label("loc_411")

    CloseMessageWindow()
    Jump("loc_4A8")

    label("loc_415")


    ChrTalk(    #2
        0xFE,
        (
            "其实啊，\x01",
            "我这次要当埃尔赛尤的专属技师了哦。\x02",
        )
    )

    Jump("loc_453")

    label("loc_453")

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "嗯，应该是那时候的缘分吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "据说也有休假，\x01",
            "所以我毫不犹豫就答应了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4A8")

    Jump("loc_5BF")

    label("loc_4AB")

    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x106, 500)
    Sleep(300)

    ChrTalk(    #5
        0xFE,
        "你、你是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "好像是在埃尔赛尤上\x01",
            "遇到的游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#050F哦……\x02\x03",

            "#051F这么说来，\x01",
            "在飞艇坠落的时候，\x01",
            "受了你们技术人员不少照顾呢。\x02\x03",

            "多谢啦。\x02",
        )
    )

    Jump("loc_57E")

    label("loc_57E")

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "哈哈，没什么没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "这也是我们的工作嘛。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x10)
    OP_A2(0x2F8C)

    label("loc_5BF")

    TalkEnd(0xFE)
    Return()

    # Function_3_3A4 end

    def Function_4_5C3(): pass

    label("Function_4_5C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(    #10
        0xFE,
        (
            "这里的线路就像一张网一样\x01",
            "盘绕在工房区的地下，\x01",
            "错综复杂地连接着各个工厂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "作为其终端的中央工房，\x01",
            "反而像柱子一样矗立着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "虽然很少有人知道，\x01",
            "不过这里的地下室其实是有五层的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_715")

    label("loc_697")


    ChrTalk(    #13
        0xFE,
        (
            "我在地下的导力器工厂\x01",
            "当过现场主任……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "不过现在暂时\x01",
            "转到这边工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "现在正在听菲小姐\x01",
            "说明业务的流程。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_715")

    TalkEnd(0xFE)
    Return()

    # Function_4_5C3 end

    def Function_5_719(): pass

    label("Function_5_719")

    Call(0, 6)
    Return()

    # Function_5_719 end

    def Function_6_71E(): pass

    label("Function_6_71E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_7F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_788")

    ChrTalk(    #16
        0x14,
        (
            "要找艾莉卡博士的话，\x01",
            "她刚才乘升降梯离开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "虽然不知道\x01",
            "是往哪里去的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F9")

    label("loc_788")


    ChrTalk(    #18
        0x14,
        (
            "…………咦？\x01",
            "要找艾莉卡博士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        "嗯嗯，刚才她的确经过这里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "和提妲一起\x01",
            "乘升降梯离开了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_7F9")

    TalkEnd(0x14)
    Return()

    # Function_6_71E end

    def Function_7_7FD(): pass

    label("Function_7_7FD")

    Call(0, 8)
    Return()

    # Function_7_7FD end

    def Function_8_802(): pass

    label("Function_8_802")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_8BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_854")

    ChrTalk(    #21
        0x13,
        "咦，今天真是安静啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13,
        "虽然这反而令人觉得诡异……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BF")

    label("loc_854")


    ChrTalk(    #23
        0x13,
        (
            "如果在中央工房里听到奇怪的声音\x01",
            "或者爆炸声，都不要见怪哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x13,
        (
            "嗯，\x01",
            "这是我小小的建议……\x02",
        )
    )

    Jump("loc_8BB")

    label("loc_8BB")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_8BF")

    TalkEnd(0x13)
    Return()

    # Function_8_802 end

    def Function_9_8C3(): pass

    label("Function_9_8C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-170, 0, -3880, 0)
    OP_67(0, 8480, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5000, 0, 9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x107, 0, 0, -13500, 0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(2000, 0)

    def lambda_962():
        OP_6D(-3950, 0, 4690, 4000)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_962)

    def lambda_97A():
        OP_6C(40000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_97A)

    def lambda_98A():
        OP_67(0, 5240, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_98A)

    def lambda_9A2():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_9A2)
    OP_43(0x107, 0x3, 0x0, 0xA)
    Sleep(2500)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_9CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9CE)

    def lambda_9E0():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1AC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9E0)
    WaitChrThread(0x12, 0x1)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    WaitChrThread(0x107, 0x3)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #25
        0x107,
        (
            "#061F#12P啊，工房长叔叔。\x01",
            "您早～！\x02",
        )
    )

    Jump("loc_A5A")

    label("loc_A5A")

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A78():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1112, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A78)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        (
            "#800F#5P哎、哎呀，是提妲吗。\x01",
            "早上好。\x02",
        )
    )

    Jump("loc_AD4")

    label("loc_AD4")

    CloseMessageWindow()

    ChrTalk(    #27
        0x107,
        (
            "#560F#12P那个那个，\x01",
            "您见过我妈妈和爷爷吗？\x02\x03",

            "他们好像一大早\x01",
            "就去了中央工房……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "#803F#5P啊啊，见过啊。\x01",
            "不止是见过……\x02\x03",

            "今天一大早，\x01",
            "艾莉卡博士就冲了过来……\x02\x03",

            "#804F『我要做新发明，\x01",
            "  借我够大的地方！』#3400W \x01",
            "#20W#803F还这样威胁我呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x107,
        (
            "#562F#12P对、对不起。\x02\x03",

            "妈妈每次做实验\x01",
            "都会给您添麻烦……\x02\x03",

            "#067F不过，\x01",
            "应该比爷爷要好一点吧。\x02\x03",

            "因为在爆炸之前\x01",
            "她会说『提妲，\x01",
            "堵住耳朵！』嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#801F#5P哈哈，还有这种事啊。\x01",
            "啊哈哈哈哈…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #31
        0x12,
        (
            "#800F#5P提妲，\x01",
            "艾莉卡博士现在应该在演算室。\x02\x03",

            "虽然不知道她这次要干什么，\x01",
            "但是好像正在用\x01",
            "卡佩尔调查一些事情。\x02\x03",

            "#805F拉赛尔博士应该在设计室吧。\x01",
            "他、他好像相当高兴的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    def lambda_DF5():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_DF5)
    Sleep(1000)

    ChrTalk(    #32
        0x12,
        (
            "#806F#5P唉唉，怎么搞的……\x01",
            "你说巧不巧，\x01",
            "偏偏是那两个人进行共同开发……！\x02\x03",

            "拜、拜、拜、拜托了。\x01",
            "千万别弄坏什么东西啊……\x02\x03",

            "#803F咕噜咕噜咕噜～……（胃痛）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_ECC():

        label("loc_ECC")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_ECC")

    QueueWorkItem2(0x107, 2, lambda_ECC)

    def lambda_EDD():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xBE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EDD)
    WaitChrThread(0x12, 0x1)

    def lambda_EFD():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EFD)
    WaitChrThread(0x12, 0x1)

    def lambda_F1D():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_F1D)
    Sleep(1000)

    def lambda_F3C():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xFFFFFE34, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F3C)
    WaitChrThread(0x12, 0x1)

    def lambda_F5C():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_F5C)
    Sleep(1000)

    def lambda_F7B():
        OP_8E(0xFE, 0xFFFFF31C, 0x0, 0xFFFFDE2C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F7B)
    Sleep(3000)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #33
        0x107,
        (
            "#064F#5P这么说来，\x01",
            "他们每次都为\x01",
            "『发明比赛』什么的而吵架……\x02\x03",

            "这次却要共同开发啊。\x02\x03",

            "#060F妈妈啊，\x01",
            "每次一开始工作\x01",
            "就变得有些严厉而可怕……\x02\x03",

            "但是她工作的样子又很帅，\x01",
            "是个不输给爷爷的\x01",
            "研究员哦。\x02\x03",

            "#067F嘿嘿，\x01",
            "他们俩要是合作的话会怎么样呢⊙\x02\x03",

            "要、要赶快去见识一下才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x107, 0x2)
    OP_8C(0x107, 0, 600)

    def lambda_10FC():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x1C70, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_10FC)
    WaitChrThread(0x107, 0x1)
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_1126():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x251C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1126)
    WaitChrThread(0x107, 0x1)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3119   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_8C3 end

    def Function_10_116B(): pass

    label("Function_10_116B")


    def lambda_1171():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1171)

    def lambda_1183():
        OP_8E(0xFE, 0x0, 0x0, 0xFFFFF740, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1183)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x107, 0x1)

    def lambda_11AD():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0xA78, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11AD)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 500)
    Return()

    # Function_10_116B end

    def Function_11_11CF(): pass

    label("Function_11_11CF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x05左·中央工房电梯\x01",
            "右·地下导力器工厂\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_11CF end

    def Function_12_1227(): pass

    label("Function_12_1227")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #35
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1227 end

    SaveToFile()

Try(main)
