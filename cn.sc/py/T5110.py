from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5110   ._SN',
        MapName             = 'Other',
        Location            = 'T5110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60025",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T5110   ._SN',
            'ED6_DT21/T5110_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '亚妮拉丝',                             # 9
        '克鲁茨',                               # 10
        '维修师罗伯特',                         # 11
        '菲莉斯管理员',                         # 12
        '目标用照相机',                         # 13
        '器皿',                                 # 14
        '器皿',                                 # 15
        '器皿',                                 # 16
        '咖啡',                                 # 17
        '咖啡',                                 # 18
        '艾丝蒂尔的背部',                       # 19
        '新型导力器',                           # 20
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
        'ED6_DT27/CH03090 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT27/CH03093 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03900 ._CH',             # 05
        'ED6_DT07/CH01623 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT26/CH20269 ._CH',             # 08
        'ED6_DT26/CH20235 ._CH',             # 09
        'ED6_DT27/CH03133 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT27/CH03090P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT27/CH03093P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03900P._CP',             # 05
        'ED6_DT07/CH01623P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT26/CH20269P._CP',             # 08
        'ED6_DT26/CH20235P._CP',             # 09
        'ED6_DT27/CH03133P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 12470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638407,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245192,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 917512,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 120250,
        Y                   = 0,
        Z                   = 1000,
        Range               = 123170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22500,
        TriggerZ            = 0,
        TriggerY            = 12360,
        TriggerRange        = 800,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 12470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15050,
        TriggerZ            = 0,
        TriggerY            = 12130,
        TriggerRange        = 800,
        ActorX              = 15050,
        ActorZ              = 1000,
        ActorY              = 12130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113640,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 113040,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_356",          # 00, 0
        "Function_1_4E2",          # 01, 1
        "Function_2_523",          # 02, 2
        "Function_3_5CA",          # 03, 3
        "Function_4_5CF",          # 04, 4
        "Function_5_5D4",          # 05, 5
        "Function_6_A98",          # 06, 6
        "Function_7_128C",         # 07, 7
        "Function_8_1607",         # 08, 8
        "Function_9_2D3E",         # 09, 9
        "Function_10_2D96",        # 0A, 10
    )


    def Function_0_356(): pass

    label("Function_0_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_360")
    Jump("loc_445")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_445")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_374")
    Jump("loc_445")

    label("loc_374")

    SetChrPos(0x8, 115980, 0, 37820, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 84690, 0, -30350, 0)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrPos(0xB, 25910, 0, 16520, 0)
    SetChrPos(0xA, 27980, 0, 6920, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_END)), "loc_3D7")
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3D7")

    SetChrPos(0xD, 18160, 800, 11990, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, 17670, 800, 12040, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 17600, 800, 11180, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, 18270, 800, 10980, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 18190, 800, 11550, 0)
    ClearChrFlags(0xF, 0x80)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9")
    OP_44(0x9, 0xFF)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x9, 15080, 200, 14890, 180)
    SetChrPos(0x8, 13670, 200, 12380, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0x8, 2)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_4B7")
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4C5")
    OP_A3(0x10F1)
    Event(0, 6)

    label("loc_4C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E1")
    Event(0, 7)

    label("loc_4E1")

    Return()

    # Function_0_356 end

    def Function_1_4E2(): pass

    label("Function_1_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_END)), "loc_500")
    OP_64(0x2, 0x1)
    Jump("loc_522")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_516")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jump("loc_522")

    label("loc_516")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_522")

    Return()

    # Function_1_4E2 end

    def Function_2_523(): pass

    label("Function_2_523")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5B4")

    label("loc_560")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5B4")

    label("loc_56C")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5B4")

    label("loc_578")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5B4")

    label("loc_584")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B4")

    label("loc_590")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5B4")

    label("loc_59C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5C9")

    Return()

    # Function_2_523 end

    def Function_3_5CA(): pass

    label("Function_3_5CA")

    Call(1, 4)
    Return()

    # Function_3_5CA end

    def Function_4_5CF(): pass

    label("Function_4_5CF")

    Call(1, 5)
    Return()

    # Function_4_5CF end

    def Function_5_5D4(): pass

    label("Function_5_5D4")

    EventBegin(0x0)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0xD, 18160, 800, 11990, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, 17670, 800, 12040, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 17600, 800, 11180, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, 18270, 800, 10980, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 18190, 800, 11550, 0)
    ClearChrFlags(0xF, 0x80)
    FadeToBright(1000, 0)

    def lambda_6D5():
        OP_6D(18760, 200, 12150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D5)

    def lambda_6ED():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ED)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#1016F呼……\x01",
            "肚子吃得饱饱的。\x02\x03",

            "演习前吃这么多\x01",
            "好像不太好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#811F#5P呵呵，管理员做的料理\x01",
            "真的是很美味嘛。\x02\x03",

            "#816F不过，这次演习和训练不同，\x01",
            "中途是不能够休息的，\x01",
            "吃饱点不是正好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1006F嗯，的确。\x01",
            "毕竟体力是一切的基础嘛。\x02\x03",

            "#1015F话说回来……\x01",
            "来到这里已经３周了吗。\x02\x03",

            "老实说，还真是一转眼的功夫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#810F#5P呵呵，艾丝蒂尔\x01",
            "真是非常努力呢。\x02\x03",

            "我和你一起训练…\x01",
            "真的，感觉太棒了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1008F嘿嘿……\x01",
            "听你这么说我也很高兴。\x02\x03",

            "#1006F不过，克鲁茨前辈\x01",
            "会来到这里当训练教官\x01",
            "已经够让人吃惊了……\x02\x03",

            "亚妮拉丝竟然也会\x01",
            "和我一起接受训练，\x01",
            "实在是想都想不到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#818F#5P嗯～我当上正游击士\x01",
            "也才半年左右，还是个新手嘛。\x02\x03",

            "#810F从雪拉前辈那里听说了\x01",
            "艾丝蒂尔的事，\x01",
            "就觉得这是个很好的机会。\x02\x03",

            "以前听前辈们提过这个训练场之后，\x01",
            "我就一直很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1011F是吗……\x02\x03",

            "#1015F不过，竟然会有这种地方，\x01",
            "看来协会也是相当大的组织呢。\x02\x03",

            "一开始听老爸他们说的时候\x01",
            "还没有什么感觉……\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5D4 end

    def Function_6_A98(): pass

    label("Function_6_A98")

    ClearMapFlags(0x2000000)
    OP_BB(0x0, 0x0, 0x200032)
    OP_BB(0x0, 0x1, 0x0)
    OP_BD()
    EventBegin(0x0)
    OP_6D(18760, 200, 12150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    FadeToBright(1000, 0)
    OP_1F(0x64, 0x3E8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #7
        0x8,
        (
            "#810F#5P原来如此……\x02\x03",

            "那套衣服，是雪拉前辈\x01",
            "的祝贺礼物啊。\x02\x03",

            "#811F好羡慕～\x01",
            "给你买这么可爱的衣服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1013F嗯、嗯……\x02\x03",

            "布料相当结实，\x01",
            "活动起来也很方便……\x02\x03",

            "不过这种女性化的衣服\x01",
            "大概不适合我吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#816F#5P才没这回事！\x01",
            "非常非常适合你哦。\x02\x03",

            "而且就算是游击士，\x01",
            "女孩子也需要好好打扮哦。\x02\x03",

            "#815F不，正因为是游击士\x01",
            "所以才必须要认真地打扮！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F亚、亚妮拉丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1310F#5P对了，艾丝蒂尔。\x01",
            "想不想扎个丝带看看？\x02\x03",

            "#811F我想一定很好看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1008F心、心领了。\x02\x03",

            "#1016F话说回来……\x01",
            "以前我就一直在想。\x02\x03",

            "亚妮拉丝你\x01",
            "是不是对可爱的东西毫无免疫力？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#811F#5P当然了！\x01",
            "可爱即是正义嘛！\x02\x03",

            "#1310F虽然像雪拉前辈那样\x01",
            "帅气的大姐姐也很令人向往……\x02\x03",

            "不过终究还是比不上\x01",
            "打扮可爱的小女孩啊！\x02\x03",

            "#1311F如果再抱着布偶之类的东西…\x01",
            "就让人更想紧紧地抱住了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "（她要是见到提妲的话，\x01",
            "  说不定会激动得昏倒呢……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1314F#5P嘻嘻，话说回来……\x02\x03",

            "和第一次相遇时比起来，\x01",
            "艾丝蒂尔，你变了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1004F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#817F#5P一开始就是个新人，\x01",
            "给人一副涉世未深的印象……\x02\x03",

            "现在，虽然还是涉世未深，\x01",
            "但给人的感觉却更加可靠了。\x02\x03",

            "#816F你可真厉害哦～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1008F讨、讨厌啦……\x01",
            "亚妮拉丝，不要奉承我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#811F#5P啊哈哈，别害羞别害羞。\x02\x03",

            "#816F嗯，作为前辈\x01",
            "我也不能输给你啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1013F真是的……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x101,
        (
            "#1004F对了，亚妮拉丝。\x01",
            "差不多到演习的时间了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#814F#5P啊，是哦。\x01",
            "先回房间吧。\x02\x03",

            "#811F那么，一会儿见～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x101, 2)
    OP_8E(0x8, 0x5154, 0x0, 0x2472, 0xBB8, 0x0)

    def lambda_10CD():
        OP_8E(0x8, 0x6CAC, 0x7D0, 0x2346, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10CD)

    def lambda_10E8():
        OP_6D(20870, 200, 10700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10E8)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)

    def lambda_110A():
        OP_8E(0x8, 0x6C84, 0x7D0, 0x2ABC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_110A)
    WaitChrThread(0x8, 0x1)

    def lambda_112A():
        OP_8E(0x8, 0x63D8, 0xDAC, 0x2C1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_112A)

    def lambda_1145():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1145)
    WaitChrThread(0x8, 0x1)

    def lambda_115C():
        OP_6D(18770, 200, 11170, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_115C)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x8, 0x80)

    ChrTalk(    #23
        0x101,
        (
            "#5P#1017F呼～真是个充满朝气的人。\x02\x03",

            "和亚妮拉丝在一起，\x01",
            "我也轻松多了呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        (
            "#5P#1006F好了，我也回房间\x01",
            "准备一下必要的装备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x363, 1)
    OP_3E(0x35D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 19120, 0, 10210, 103)
    OP_A2(0x1004)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_A98 end

    def Function_7_128C(): pass

    label("Function_7_128C")

    EventBegin(0x0)
    OP_6D(87090, 0, 40680, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 86470, 0, 35830, 0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x12, 84860, 100, 41540, 0)
    SetChrChipByIndex(0x12, 8)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)

    def lambda_1320():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1320)
    OP_8E(0x101, 0x151EE, 0x0, 0x922C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x101,
        (
            "#1015F#5P那么，既然是演习，\x01",
            "一般的装备还是必要的吧。\x02\x03",

            "毕竟和实战一样，\x01",
            "也不知道会发生什么……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13B3():
        OP_6D(87290, 0, 42930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13B3)

    def lambda_13CB():
        OP_67(0, 6050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CB)

    def lambda_13E3():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13E3)
    OP_8E(0x101, 0x150B8, 0x0, 0xA2EE, 0x7D0, 0x0)
    OP_8C(0x101, 261, 500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        "\x07\x05艾丝蒂尔从背包里取出了口琴。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Fade(500)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 7)
    OP_0D()

    ChrTalk(    #27
        0x101,
        (
            "#5P#1025F……………………………\x02\x03",

            "#1012F嗯，今天也要加油。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x12, 0x80)
    OP_D6(0x1)
    OP_3E(0x35F, 1)
    OP_3E(0x363, 1)
    OP_3E(0x35D, 1)
    OP_3E(0x411, 1)
    AddMira(1000)
    OP_41(0x0, 0x9, 0xFF)
    OP_41(0x0, 0x104, 0xFF)
    OP_41(0x0, 0x125, 0xFF)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #28
        "\x07\x00得到了\x1F\x11\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x1F\x09\x00\x07\x00装备了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #30
        "\x1F\x04\x01\x07\x00装备了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x1F\x25\x01\x07\x00装备了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 3)), scpexpr(EXPR_END)), "loc_15A2")
    OP_3E(0x417, 1)
    OP_A3(0x22B3)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x07\x00得到了\x1F\x17\x04\x07\x00。\x02",
    )

    CloseMessageWindow()

    label("loc_15A2")

    OP_22(0x14, 0x0, 0x64)

    AnonymousTalk(    #33
        "\x07\x00得到了\x07\x04１０００\x07\x00米拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #34
        0x101,
        (
            "#5P#1006F这样就好了。\x02\x03",

            "……那么\x01",
            "去大门吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1005)
    EventEnd(0x0)
    Return()

    # Function_7_128C end

    def Function_8_1607(): pass

    label("Function_8_1607")

    EventBegin(0x0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 15080, 200, 12380, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 1)
    OP_6D(15150, 0, 14940, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(    #35
        0x9,
        (
            "#843F来了吗，艾丝蒂尔。\x01",
            "那么现在马上开始演习吧。\x02\x03",

            "#842F今天的演习是遗迹探索。\x02\x03",

            "你们要进入宿舍西边的\x01",
            "『巴斯塔尔水道』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1745")

    label("loc_16FB")


    ChrTalk(    #36
        0x9,
        (
            "#842F今天的演习是遗迹探索。\x02\x03",

            "你们要进入宿舍西边的\x01",
            "『巴斯塔尔水道』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1745")


    ChrTalk(    #37
        0x101,
        (
            "#1002F『巴斯塔尔水道』……\x02\x03",

            "好古老的名字，\x01",
            "是训练用的设施吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#840F啊啊。\x01",
            "是在中世纪遗迹上重建而成的设施。\x02\x03",

            "里面遗留着从前的机关，\x01",
            "同时也游荡着大量危险的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#816F#6P原——来如此。\x01",
            "看起来相当接近实战呢。\x02\x03",

            "那么我们就\x01",
            "马上出发前往那个水道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#843F不，在那之前……\x02\x03",

            "#842F你们两人先看看这个。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #41
        "\x07\x05克鲁茨取出了陌生形状的导力器。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0x13, 0x4)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0x13, 14500, 150, 13630, 180)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 1)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x24008F, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #42
        "\x07\x00#1004F咦，这是……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #43
        (
            "\x07\x00#814F#6P难不成……\x01",
            "是战术导力器吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName("克鲁茨")

    AnonymousTalk(    #44
        (
            "\x07\x00#840F嗯嗯，没错。\x02\x03",

            "可以使用导力魔法的\x01",
            "战术导力器，据说是\x01",
            "『爱普斯坦财团』制造的……\x02\x03",

            "这是在上个月\x01",
            "刚从财团送来的最新型。\x02\x03",

            "结晶孔的数量增加为７个。\x02\x03",

            "在现有的魔法基础上\x01",
            "还能组合出新型的魔法。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #45
        "\x07\x00#1006F哟～很棒嘛！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #46
        (
            "\x07\x00#811F#6P嗯嗯！\x01",
            "看来相当值得期待呢。\x02\x03",

            "#810F那，克鲁茨前辈。\x01",
            "我们也能够拿到吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName("克鲁茨")

    AnonymousTalk(    #47
        (
            "\x07\x00#840F嗯嗯，只要提出申请，\x01",
            "协会就会免费提供。\x02\x03",

            "#843F只是……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #48
        0x9,
        (
            "#842F目前有一个难题。\x02\x03",

            "新型导力器大幅改动了\x01",
            "以往基本构造。\x02\x03",

            "但是，由于兼容性的问题\x01",
            "无法安装以前的结晶回路。\x02\x03",

            "而是需要新规格的结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1004F咦咦～！？\x02\x03",

            "那、那就是说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#814F#6P以前合成的结晶回路\x01",
            "都白费了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#840F很遗憾，没有错。\x02\x03",

            "虽然相当麻烦，不过\x01",
            "只能从头一个个去收集了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1007F不，不是吧～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#1316F#6P嗯……\x01",
            "真是让人犹豫呢。\x02\x03",

            "#810F就这样继续使用\x01",
            "现在的导力器不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#843F虽然不是不行，但并不推荐。\x02\x03",

            "#842F新型导力器各方面的性能\x01",
            "都比以前的型号更高。\x02\x03",

            "不但最大ＥＰ大幅度地提高了，\x01",
            "而且适用于最新型的结晶回路。\x02\x03",

            "就前景来说，可以期待它\x01",
            "更进一步地提高身体能力。\x02\x03",

            "#843F而且不管怎么说，\x01",
            "最大优点就是在于可以组合出\x01",
            "以前的导力器所没有的新魔法。\x02\x03",

            "#842F……艾丝蒂尔。\x01",
            "你还记得洛伦斯少尉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1020F哎！？\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400BF, 0x0, 0x0, 0xC8)
    Sleep(2000)
    OP_AE(0xC8)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        (
            "#1026F嗯、嗯。\x02\x03",

            "这个对手让人\x01",
            "想忘都忘不掉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#842F雪拉告诉过我，\x01",
            "他似乎使用了未知的魔法吧。\x02\x03",

            "除了大范围攻击对手之外，\x01",
            "还能带来混乱效果的高级魔法……\x02\x03",

            "其实，新型导力器\x01",
            "也可以组合出这种魔法哦。\x02\x03",

            "名为『银色荆棘』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1002F『银色荆棘』……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x8,
        (
            "#812F#6P这、这么说……\x02\x03",

            "那个蒙面队长\x01",
            "早就在使用新型的导力器吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "#843F很有可能。\x02\x03",

            "#842F好了，你们怎么决定？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#813F#6P呜……嗯，\x01",
            "果然还是很犹豫呢。\x02\x03",

            "就前景方面虽然是新型胜出，\x01",
            "但目前的战力下降实在让人心痛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1010F……………………………\x02\x03",

            "#1011F我……\x01",
            "想试着运用新型导力器。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #63
        0x8,
        "#814F#6P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1003F那个时候，我完全\x01",
            "无法对抗那名银发男子。\x02\x03",

            "更换导力器的话，\x01",
            "虽然并不代表可以让自己变强……\x02\x03",

            "#1002F但是我还是希望能\x01",
            "试着将更强大的力量运用自如。\x02\x03",

            "所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#814F#6P艾丝蒂尔……\x02\x03",

            "#816F……嗯，说得是啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(400)

    ChrTalk(    #66
        0x8,
        (
            "#1310F#6P克鲁茨前辈。\x01",
            "请让我也使用新型的吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#841F好吧。\x02\x03",

            "那么收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    ClearChrFlags(0x13, 0x80)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x05得到新型战术导力器。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x20A, 1)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #69
        0x9,
        "#840F还有，给你们这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #70
        "\x07\x05得到了各属性的耀晶片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x64)
    AddSepith(0x6, 0x14)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #71
        0x9,
        (
            "#840F只要有这些\x01",
            "基本的结晶回路就齐了吧。\x02\x03",

            "去演习之前，到那边的工房\x01",
            "请罗伯特合成就好了。\x02\x03",

            "新的结晶回路和导力魔法列表\x01",
            "已经追加在游击士手册里了。\x02\x03",

            "去工房的时候\x01",
            "自己去确认吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006F嗯，明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#840F还有……\x01",
            "今天的演习应该过程较长。\x02\x03",

            "为预防万一，\x01",
            "最好连食材也准备好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#818F#6P嗯～食材啊……\x02\x03",

            "#816F这个去找菲莉斯小姐\x01",
            "就ＯＫ了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "#843F啊啊，是啊。\x02\x03",

            "罗伯特先生和菲莉斯管理员……\x01",
            "询问他们两人后再进行准备吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2495")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x34), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2488")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2492")

    label("loc_2488")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2492")

    Jump("loc_24C4")

    label("loc_2495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24C4")

    label("loc_24AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29CC")
    Sleep(500)

    ChrTalk(    #76
        0x9,
        (
            "#840F好了，艾丝蒂尔\x01",
            "顺便也收下这个。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (1, "loc_2522"),
        (2, "loc_2699"),
        (3, "loc_27C4"),
        (4, "loc_28CC"),
        (SWITCH_DEFAULT, "loc_29C3"),
    )


    label("loc_2522")

    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_3E(0x140, 1)
    OP_3E(0x2D9, 1)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #77
        "\x07\x00得到了\x1F\x4F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x07\x00得到了\x1F\x40\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #80
        "\x07\x00得到了\x1F\xD9\x02\x07\x00结晶回路。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #81
        0x101,
        "#1004F咦，这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#1310F#6P啊，好羡慕～\x02\x03",

            "#811F而且是相当\x01",
            "好的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#841F啊啊，都是特别定制的。\x02\x03",

            "当然结晶回路\x01",
            "是新型导力器用的。\x02\x03",

            "就当作是协会对于你之前\x01",
            "准游击士的功绩所给予的报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1008F嘿嘿，谢谢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_2699")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_3E(0x140, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00得到了\x1F\x4F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #86
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #87
        "\x07\x00得到了\x1F\x40\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #88
        0x101,
        "#1004F咦，这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#1310F#6P啊，好羡慕～\x02\x03",

            "#811F而且是相当\x01",
            "好的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#841F啊啊，每个都是特别定制的。\x02\x03",

            "就当是由于准游击士的功绩\x01",
            "行会给予的报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1008F嘿嘿，谢谢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_27C4")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #92
        "\x07\x00得到了\x1F\x4F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #94
        0x101,
        "#1004F咦，这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "#1310F#6P啊，好羡慕～\x02\x03",

            "#811F而且是相当\x01",
            "好的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "#841F啊啊，是特别定制的。\x02\x03",

            "就当是由于准游击士的功绩\x01",
            "行会给予的报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1008F嘿嘿，谢谢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_28CC")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #98
        "\x07\x00得到了\x1F\x4F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #99
        0x101,
        "#1004F咦，这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#1310F#6P啊，好羡慕～\x02\x03",

            "#811F而且看来是\x01",
            "相当好的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#841F嗯嗯，是特别定制的。\x02\x03",

            "就当作是协会对你之前\x01",
            "准游击士的功绩所给予的报酬吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1008F嘿嘿，谢谢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_29C3")

    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_29CC")

    Sleep(500)

    ChrTalk(    #103
        0x9,
        (
            "#840F那么我就在\x01",
            "宿舍的出口等你们。\x02\x03",

            "准备完毕的话就过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrPos(0x9, 16210, 0, 14960, 93)
    ClearChrFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 3)
    OP_0D()

    def lambda_2A42():
        OP_6D(18450, 0, 12380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A42)
    SetChrSubChip(0x8, 2)

    def lambda_2A5F():
        OP_8E(0x9, 0x48DA, 0x0, 0x38A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A5F)
    Sleep(500)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x9, 0x0)

    def lambda_2A89():
        OP_8E(0x9, 0x5294, 0x0, 0x2E86, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A89)
    WaitChrThread(0x9, 0x1)

    def lambda_2AA9():
        OP_8E(0x9, 0x53E8, 0xFFFFFED4, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2AA9)
    WaitChrThread(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)

    def lambda_2AD3():
        OP_6D(14220, 600, 12150, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AD3)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #104
        0x8,
        (
            "#816F#6P那么，艾丝蒂尔。\x01",
            "我们马上开始演习的准备吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #105
        0x101,
        (
            "#1006F#2P嗯，要去菲莉斯小姐\x01",
            "和罗伯特先生那里\x01",
            "询问他们一下才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    AddParty(0x9, 0xF7, 0xFF)
    SetChrPos(0x101, 16020, 0, 11870, 160)
    SetChrPos(0x10A, 16020, 0, 11870, 160)
    OP_6D(16020, 0, 11870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_41(0x9, 0xCF, 0xFF)
    OP_41(0x9, 0x104, 0xFF)
    OP_41(0x9, 0x125, 0xFF)
    OP_BB(0x9, 0x6, 0x110)
    OP_31(0x9, 0x0, 0x28)
    OP_31(0x9, 0xFE, 0x0)
    OP_35(0x9, 0x0)
    Sleep(500)
    OP_64(0x2, 0x1)
    OP_A2(0x1006)
    OP_28(0xC5, 0x4, 0x2)
    OP_28(0xC5, 0x4, 0x8)
    OP_28(0xC5, 0x1, 0x1)
    OP_28(0xC5, 0x1, 0x2)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #106
        (
            "\x07\x05※『正游击士手册』（游击士手册）能够使用了。\x01",
            "　工作上的事情和导力器的详细说明\x01",
            "　都可以参考这本手册。\x02\x03",

            "※游击士手册的打开方法：在整备画面内［Item］栏\x01",
            "  的［书籍］分类标签当中使用『正游击士手册』，\x01",
            "  或是点选画面右下角的图示（蓝）。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_1607 end

    def Function_9_2D3E(): pass

    label("Function_9_2D3E")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #107
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_2D3E end

    def Function_10_2D96(): pass

    label("Function_10_2D96")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "休息\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1D")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_8C(0x0, 270, 0)
    OP_30(0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2E1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E37")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2E37")

    Return()

    # Function_10_2D96 end

    SaveToFile()

Try(main)
