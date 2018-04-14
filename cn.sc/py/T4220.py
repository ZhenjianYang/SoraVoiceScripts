from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '艾莉茜雅女王',                         # 9
        '摩尔根将军',                           # 10
        '雪拉扎德',                             # 11
        '奥利维尔',                             # 12
        '科洛蒂娅公主',                         # 13
        '阿加特',                               # 14
        '提妲',                                 # 15
        '金',                                   # 16
        '凯文神父',                             # 17
        '卡西乌斯',                             # 18
        '尤莉亚上尉',                           # 19
        '王国军士官',                           # 20
        '基库',                                 # 21
        '希德中校',                             # 22
        '理查德',                               # 23
        '亲卫队队员',                           # 24
        '布莉姆',                               # 25
        '目标用照相机',                         # 26
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
        'ED6_DT07/CH02013 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT27/CH03080 ._CH',             # 08
        'ED6_DT27/CH03670 ._CH',             # 09
        'ED6_DT27/CH03580 ._CH',             # 0A
        'ED6_DT07/CH01600 ._CH',             # 0B
        'ED6_DT07/CH02010 ._CH',             # 0C
        'ED6_DT26/CH20411 ._CH',             # 0D
        'ED6_DT26/CH20432 ._CH',             # 0E
        'ED6_DT07/CH00041 ._CH',             # 0F
        'ED6_DT07/CH00061 ._CH',             # 10
        'ED6_DT07/CH01350 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH02013P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT27/CH03080P._CP',             # 08
        'ED6_DT27/CH03670P._CP',             # 09
        'ED6_DT27/CH03580P._CP',             # 0A
        'ED6_DT07/CH01600P._CP',             # 0B
        'ED6_DT07/CH02010P._CP',             # 0C
        'ED6_DT26/CH20411P._CP',             # 0D
        'ED6_DT26/CH20432P._CP',             # 0E
        'ED6_DT07/CH00041P._CP',             # 0F
        'ED6_DT07/CH00061P._CP',             # 10
        'ED6_DT07/CH01350P._CP',             # 11
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 320,
        Z                   = 0,
        Y                   = 141880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_3D1",          # 01, 1
        "Function_2_3F7",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_535",          # 04, 4
        "Function_5_340A",         # 05, 5
        "Function_6_3450",         # 06, 6
        "Function_7_347B",         # 07, 7
        "Function_8_34A6",         # 08, 8
        "Function_9_34C7",         # 09, 9
        "Function_10_34E8",        # 0A, 10
        "Function_11_3509",        # 0B, 11
        "Function_12_352A",        # 0C, 12
        "Function_13_354B",        # 0D, 13
        "Function_14_3576",        # 0E, 14
        "Function_15_35A1",        # 0F, 15
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_389")
    SetChrFlags(0x18, 0x80)
    Jump("loc_395")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_395")
    SetChrFlags(0x18, 0x80)

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_3D0")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3D0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_3D0")

    Return()

    # Function_0_37A end

    def Function_1_3D1(): pass

    label("Function_1_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ED")
    OP_B1("t4220_y")
    Jump("loc_3F6")

    label("loc_3ED")

    OP_B1("t4220_n")

    label("loc_3F6")

    Return()

    # Function_1_3D1 end

    def Function_2_3F7(): pass

    label("Function_2_3F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A")
    OP_8D(0xFE, -2480, 144940, 3210, 138830, 2000)
    Jump("Function_2_3F7")

    label("loc_41A")

    Return()

    # Function_2_3F7 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_428")
    Jump("loc_531")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4DD")

    ChrTalk(    #0
        0xFE,
        (
            "哼，杜南公爵\x01",
            "返回城堡了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "在要塞照顾上校都\x01",
            "比现在好上一千倍～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "……不过公爵先生\x01",
            "不再直直地\x01",
            "盯着别人看了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "唉……不知道是不是因为\x01",
            "最近布莉姆发胖了～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_531")

    ChrTalk(    #4
        0xFE,
        (
            "公爵去离宫生活之后\x01",
            "我可轻松了不少～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "因为公爵\x01",
            "会直直地盯着\x01",
            "别人看～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531")

    TalkEnd(0xFE)
    Return()

    # Function_3_41B end

    def Function_4_535(): pass

    label("Function_4_535")

    EventBegin(0x0)
    OP_6D(840, 500, 153020, 0)
    OP_67(0, 5330, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    SetChrPos(0x8, 40, 750, 155220, 180)
    SetChrPos(0x9, 1350, 500, 153580, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 610, 0, 150320, 0)
    SetChrPos(0x102, -590, 0, 150300, 0)
    SetChrFlags(0x18, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x102,
        (
            "#1035F#6P──以上就是我在迄今为止的独自行动中，\x01",
            "以及潜入方舟时所掌握到的一切情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#163F#5P唔……这真令人惊讶。\x02\x03",

            "想不到会有那种怪物级的飞船\x01",
            "侵入了利贝尔……\x02\x03",

            "#166F他们拿出那种东西\x01",
            "究竟打算干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1043F#6P『福音计划』的全貌\x01",
            "目前还是无法尽窥。\x02\x03",

            "#1042F但他们已经开始\x01",
            "下一步行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F#4P我记得……\x01",
            "好像是叫第三阶段。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#094F#5P现在真是事态紧急呢……\x02\x03",

            "#093F摩尔根将军。\x01",
            "王国军将有什么应对？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #11
        0x9,
        (
            "#165F#2P这两人昨晚\x01",
            "已经联络了卡西乌斯。\x02\x03",

            "在他的指示下，王国军全体\x01",
            "已经进入到了一级警戒体制。\x02\x03",

            "另外还出动了飞行舰队\x01",
            "在王国全境进行巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#090F#5P是吗……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #13
        0x8,
        (
            "#090F艾丝蒂尔，约修亚。\x01",
            "真是有劳你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F#4P不、不不。\x01",
            "我们只是做了理所应当的联络而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#1043F#6P说实话……我应该\x01",
            "早些联络大家才对。\x02\x03",

            "包括空贼艇抢夺事件在内，\x01",
            "真的是非常抱歉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #16
        0x101,
        "#1020F#2P等、等等，约修亚。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#1054F#6P没关系，艾丝蒂尔。\x02\x03",

            "#1053F我已经有接受\x01",
            "制裁的觉悟了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #18
        0x9,
        (
            "#166F#2P唔……\x01",
            "陛下，您意下如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#094F#5P嗯……\x01",
            "虽然有点超越法规，\x02\x03",

            "#090F不过这次多亏约修亚向我们提供了\x01",
            "有关『结社』的大量情报……\x02\x03",

            "因此，功过相抵，\x01",
            "过去的事情就不用再追究了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A43():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A43)
    Sleep(100)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #20
        0x101,
        "#1018F#4P是、是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#1042F#6P可是……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrPos(0x8, 10, 500, 154550, 180)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_AB9():
        OP_6D(840, 500, 152500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AB9)

    def lambda_AD1():
        OP_8F(0xFE, 0xFFFFFFF6, 0x1F4, 0x25328, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AD1)
    Sleep(500)

    def lambda_AF1():

        label("loc_AF1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AF1")

    QueueWorkItem2(0x9, 1, lambda_AF1)
    WaitChrThread(0x8, 0x1)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x8,
        (
            "#090F#5P没关系的，约修亚。\x02\x03",

            "#094F这样的裁决……\x01",
            "还不足以弥补你这位『哈梅尔』\x01",
            "遗孤所经受之痛苦的万分之一啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1004F#4P啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1043F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#094F#5P……看来你\x01",
            "早已知道了吧。\x02\x03",

            "#093F我虽然\x01",
            "了解那次虐杀事件的真相，\x01",
            "但却至今保持着沉默……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x101,
        (
            "#1020F#4P啊！？\x02\x03",

            "这、这是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, -180, 400)
    Sleep(500)

    ChrTalk(    #27
        0x9,
        (
            "#166F#5P战争开始时，埃雷波尼亚向\x01",
            "利贝尔发来了宣战公告……\x02\x03",

            "他们坚决指称哈梅尔村\x01",
            "发生的大屠杀\x01",
            "是王国军所为。\x02\x03",

            "#163F但战争临近结束前，帝国政府\x01",
            "却突然撤回了那项指控，\x01",
            "并提出了即刻停战的要求。\x02\x03",

            "#160F……而他们的条件，就是\x01",
            "要我们对哈梅尔事件永远保持沉默。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1020F#4P#3S！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#094F#5P……我分析了事情的前因后果，\x01",
            "大概可以想象得到在帝国内部\x01",
            "发生了怎样的事态。\x02\x03",

            "#093F反攻作战虽然取得了成功，\x01",
            "但帝国军仍然保有相当的兵力。\x02\x03",

            "如果他们从帝国本土派来增援的话，\x01",
            "王国必定将会再次陷入困境──\x02\x03",

            "#094F在这样的考虑下……\x01",
            "最终我决定接受了那个条件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1026F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1043F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#092F#5P……我为了本国的安宁\x01",
            "而放弃了对真相的追究。\x02\x03",

            "背叛了那些无辜的受害者，\x01",
            "没能为他们平息惨死的怨念。\x02\x03",

            "#094F那个时候，洛伦斯少尉曾对我说过：\x01",
            "『你没有怜悯我的资格』……\x02\x03",

            "那话真的是一针见血啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1026F#4P女王陛下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1035F#6P……请您\x01",
            "不要再自责了。\x02\x03",

            "#1040F那次虐杀事件与您完全无关，\x01",
            "而且您身为一国之主，将国家的和平\x02\x03",

            "摆在首位本就是最合理的决定。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #35
        0x8,
        "#093F#5P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1053F#6P这个叫做利贝尔的国家\x01",
            "使我这颗被冰封的心得到了温暖、痊愈，\x01",
            "可以说是我的第二故乡。\x02\x03",

            "#1040F全靠陛下的决断，这片土地才能获得安宁，\x01",
            "对此我只有感谢，又何来怨恨呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1025F#2P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#096F#5P谢谢你……约修亚。\x02\x03",

            "听你这么一说，\x01",
            "我长年以来的愧疚终于稍有减轻了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, 520, 0, 138480, 0)
    SetChrPos(0xE, -850, 0, 138320, 0)
    SetChrPos(0xA, -2560, 0, 137730, 0)
    SetChrPos(0xD, -2280, 0, 136550, 0)
    SetChrPos(0xB, 1570, 0, 138000, 0)
    SetChrPos(0xF, 2440, 0, 137650, 0)
    Sleep(500)

    NpcTalk(    #39
        0xC,
        "女孩的声音",
        "#1P艾丝蒂尔，约修亚！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_123E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_123E)
    Sleep(100)
    OP_8C(0x102, 180, 400)

    ChrTalk(    #40
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1044F#5P大家……\x02",
    )

    CloseMessageWindow()

    def lambda_1286():
        OP_6D(1130, 0, 150940, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1286)

    def lambda_129E():
        OP_67(0, 5380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_129E)

    def lambda_12B6():
        OP_6B(2770, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12B6)

    def lambda_12C6():
        OP_6E(344, 2000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_12C6)
    OP_43(0xC, 0x0, 0x0, 0x6)
    Sleep(300)
    OP_43(0xE, 0x0, 0x0, 0x7)
    Sleep(300)
    OP_43(0xA, 0x0, 0x0, 0x8)
    Sleep(300)
    OP_43(0xD, 0x0, 0x0, 0x9)
    Sleep(300)
    OP_43(0xB, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0xF, 0x0, 0x0, 0xB)
    WaitChrThread(0xC, 0x0)
    Sleep(500)

    NpcTalk(    #42
        0xC,
        "科洛丝",
        (
            "#041F#4P艾丝蒂尔！你没事真是太好了……\x02\x03",

            "#048F还有……约修亚也……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #43
        0xE,
        (
            "#067F#6P太、太好了……\x01",
            "两个人一起平安归来……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#1054F#5P科洛丝、提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1025F#5P我让你们……\x01",
            "担心了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #46
        0xA,
        (
            "#027F#6P真是的……\x01",
            "你还真会让人担惊受怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "#051F#6P嘿嘿……\x02\x03",

            "不过能把这个离家出走的坏孩子\x01",
            "顺利抓回来就比什么都好啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#1040F#5P雪拉姐、阿加特……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x0)

    ChrTalk(    #49
        0xF,
        (
            "#070F#4P两个人全都……\x01",
            "平安回来了啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#031F#2P呵呵，这也是\x01",
            "女神的引导吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1016F#5P嘿嘿……\x01",
            "抱歉，让大家担心了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, 40, 0, 140750, 0)

    NpcTalk(    #52
        0x10,
        "青年的声音",
        "#1P一点也没错。\x02",
    )

    CloseMessageWindow()

    def lambda_1548():
        OP_6D(1130, 0, 150500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1548)

    def lambda_1560():

        label("loc_1560")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1560")

    QueueWorkItem2(0xB, 1, lambda_1560)

    def lambda_1571():

        label("loc_1571")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1571")

    QueueWorkItem2(0xF, 1, lambda_1571)
    Sleep(50)

    def lambda_1587():

        label("loc_1587")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1587")

    QueueWorkItem2(0xA, 1, lambda_1587)

    def lambda_1598():

        label("loc_1598")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1598")

    QueueWorkItem2(0xD, 1, lambda_1598)
    Sleep(50)

    def lambda_15AE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_15AE)

    def lambda_15BC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15BC)
    Sleep(50)

    def lambda_15CF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15CF)
    OP_8C(0x101, 180, 400)
    ClearChrFlags(0x10, 0x80)

    def lambda_15E9():
        OP_8E(0x10, 0xFFFFFEC0, 0x0, 0x24400, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_15E9)
    Sleep(500)
    OP_43(0xC, 0x0, 0x0, 0xD)
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0xE)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0xE, 0x0)
    OP_44(0xB, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xC, 0x1)

    def lambda_1643():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1643)

    def lambda_1651():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1651)
    Sleep(50)

    def lambda_1664():

        label("loc_1664")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_1664")

    QueueWorkItem2(0xA, 1, lambda_1664)

    def lambda_1675():

        label("loc_1675")

        OP_8C(0xFE, 45, 400)
        OP_48()
        Jump("loc_1675")

    QueueWorkItem2(0xD, 1, lambda_1675)
    Sleep(50)

    def lambda_168B():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_168B)

    def lambda_1699():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1699)

    ChrTalk(    #53
        0x101,
        "#1004F#5P啊，凯文先生！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #54
        0x10,
        (
            "#1068F#4P艾丝蒂尔被掳走时，\x01",
            "我真是眼前一片漆黑。\x02\x03",

            "#1060F真是的……\x01",
            "不要这么吓唬人嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1025F#5P嗯……对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        "#1062F#4P那这位就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1040F#5P初次见面，凯文神父。\x01",
            "我是约修亚·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1068F#4P哇……\x01",
            "比想象中还英俊的美男子呢。\x02\x03",

            "#1064F嗯？你知道我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1053F#5P有关你的存在，\x01",
            "早已被收录到了我的情报网中。\x02\x03",

            "艾丝蒂尔数次陷入险境，\x01",
            "全都是靠你出手相救。\x02\x03",

            "#1040F真是……非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#1065F#4P嗯嗯……这没什么啦。\x02\x03",

            "#1060F既然你们已经重归于好，\x01",
            "那我也就没什么可说的了。\x02\x03",

            "#1063F不过呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18C9():
        OP_6D(840, 0, 151500, 1200)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_18C9)

    def lambda_18E1():
        OP_6B(2700, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18E1)

    def lambda_18F1():

        label("loc_18F1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_18F1")

    QueueWorkItem2(0x101, 1, lambda_18F1)

    def lambda_1902():

        label("loc_1902")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1902")

    QueueWorkItem2(0xC, 1, lambda_1902)

    def lambda_1913():

        label("loc_1913")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1913")

    QueueWorkItem2(0xF, 1, lambda_1913)
    SetChrFlags(0x10, 0x40)
    OP_8F(0x10, 0xFFFFFBF0, 0x0, 0x24856, 0x5DC, 0x0)
    OP_8C(0x10, 0, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)

    def lambda_194C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_194C)
    Sleep(100)
    OP_8C(0x101, 270, 400)
    Sleep(500)

    ChrTalk(    #61
        0x10,
        (
            "#1066F#4P（……以后可不能再把\x01",
            "这么可爱的女朋友扔下不管了哦。）\x02\x03",

            "（如果不想被我这样的害虫\x01",
            "趁虚而入的话。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        "#1054F#5P（…………我会铭记在心的。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1004F#2P？　怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 400)

    ChrTalk(    #64
        0x10,
        "#1061F#6P呀～没什么。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #65
        0x102,
        "#1049F#6P是男人之间的对话呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1019F#2P感觉你们没说什么好话啊……\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xF, 0x1)
    Sleep(500)
    SetChrPos(0x11, 40, 0, 140750, 0)

    NpcTalk(    #67
        0x11,
        "男性的声音",
        "#1P失礼了，陛下。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    ClearChrFlags(0x11, 0x80)
    Sleep(1000)

    def lambda_1B16():

        label("loc_1B16")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B16")

    QueueWorkItem2(0xB, 1, lambda_1B16)

    def lambda_1B27():

        label("loc_1B27")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B27")

    QueueWorkItem2(0xF, 1, lambda_1B27)
    Sleep(50)

    def lambda_1B3D():

        label("loc_1B3D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B3D")

    QueueWorkItem2(0xA, 1, lambda_1B3D)

    def lambda_1B4E():

        label("loc_1B4E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B4E")

    QueueWorkItem2(0xD, 1, lambda_1B4E)
    Sleep(50)

    def lambda_1B64():

        label("loc_1B64")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B64")

    QueueWorkItem2(0xE, 1, lambda_1B64)

    def lambda_1B75():

        label("loc_1B75")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B75")

    QueueWorkItem2(0xC, 1, lambda_1B75)
    Sleep(50)

    def lambda_1B8B():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B8B)

    def lambda_1B99():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B99)
    Sleep(50)
    TurnDirection(0x101, 0x11, 400)

    def lambda_1BB3():
        OP_6D(960, 0, 151060, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1BB3)

    def lambda_1BCB():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BCB)

    def lambda_1BDB():
        OP_8E(0x11, 0xFFFFFD1C, 0x0, 0x23A50, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1BDB)
    WaitChrThread(0x10, 0x1)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #68
        0x101,
        "#1025F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        "#1044F#5P父亲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "#090F#5P卡西乌斯先生，辛苦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "#165F#5P对各方面的指示都下达了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        (
            "#1125F#4P嗯，刚刚完成我就\x01",
            "马上赶来了。\x02\x03",

            "#1120F那么，我首先要稍尽一点\x01",
            "身为父亲的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1004F#5P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_1CF6():
        OP_6D(1130, 0, 151500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1CF6)

    def lambda_1D0E():

        label("loc_1D0E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1D0E")

    QueueWorkItem2(0x101, 1, lambda_1D0E)
    OP_8E(0x11, 0xFFFFFE3E, 0x0, 0x2489C, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #74
        0x11,
        (
            "#1120F#4P……虽然昨天进行过通讯，\x01",
            "但已经好久没有这么面对面地谈话了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#1035F#5P嗯……是啊。\x02\x03",

            "#1043F……对不起。\x01",
            "让您担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        (
            "#1125F#4P你早就向我坦白过一切，\x01",
            "所以从某种意义上说，我也算是共犯吧。\x02\x03",

            "#1122F虽然你没有道歉的必要……\x01",
            "但我却必须履行自己的义务！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_1E4A():
        OP_6B(2600, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E4A)
    Sleep(600)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    Fade(500)
    SetChrPos(0x11, -580, 0, 150280, 0)
    SetChrPos(0x102, -590, 0, 150200, 180)
    SetChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 24)
    SetChrChipByIndex(0x11, 13)
    SetChrFlags(0x102, 0x2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 13)
    SetChrFlags(0x102, 0x40)
    OP_0D()

    def lambda_1EC6():
        OP_99(0x102, 0x0, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1EC6)

    def lambda_1ED6():
        OP_99(0x11, 0x18, 0x27, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1ED6)
    Sleep(300)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #77
        0xE,
        "#065F#6P……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0xC,
        "科洛丝",
        "#043F#2P呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1020F#2P等、等等，老爸！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1035F#5P……没关系，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0xB, 0xF, 0x5DC)
    Sleep(500)

    ChrTalk(    #81
        0x102,
        (
            "#1040F#5P对一个离家出走的儿子来说……\x01",
            "这也是该有的惩罚。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x102,
        "卡西乌斯",
        (
            "#1125F#4P没错，知道就好。\x02\x03",

            "#1120F你给大家带来的忧虑和麻烦\x01",
            "比你自己想象中的更要严重……\x02\x03",

            "如今已经深刻体会到了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1043F#5P……嗯。\x02\x03",

            "#1035F我一直以为自己这种人根本不值得──\x01",
            "现在看来，这种想法果然是错的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x102,
        "卡西乌斯",
        (
            "#1122F#4P嗯……\x02\x03",

            "#1125F人类的一生，会受到\x01",
            "无数人的影响。\x02\x03",

            "反过来说，也会对自己周围\x01",
            "的人们造成各种影响。\x02\x03",

            "这就是『缘』──\x01",
            "『缘』在不断加深之后，就成为了『羁绊』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1044F#5P……『羁绊』……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #86
        0x102,
        "卡西乌斯",
        (
            "#1120F#4P而『羁绊』一旦形成，\x01",
            "就绝不可能割断。\x02\x03",

            "即使相隔千里，或是立场相悖，\x01",
            "也都会以某种形式永存在我们的心中……\x02\x03",

            "#1121F它的力量之强，你已经明白了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1054F#5P嗯……我真是太轻视它了。\x02\x03",

            "#1053F之前的我……\x01",
            "浑浑噩噩，什么都没看清呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1025F#2P约修亚……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #89
        0x102,
        "卡西乌斯",
        (
            "#1120F#4P呵呵，你能理解这一点，\x01",
            "这次离家出走也算没有白费。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x11, -580, 0, 150180, 0)

    def lambda_22DC():
        OP_99(0x102, 0x10, 0x14, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22DC)

    def lambda_22EC():
        OP_99(0x11, 0x28, 0x2C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_22EC)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    NpcTalk(    #90
        0x102,
        "卡西乌斯",
        (
            "#1125F#4P约修亚……\x01",
            "我的笨蛋儿子。\x02\x03",

            "你总算回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#1043F#5P父亲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1008F#2P呵……呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "#165F#5P嘿，这对傻瓜父子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "#091F#5P呵呵……真是太好了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, -40, 0, 138750, 0)

    NpcTalk(    #95
        0x12,
        "女性的声音",
        "#1P报告！\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2523():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2523)

    def lambda_2533():

        label("loc_2533")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2533")

    QueueWorkItem2(0xB, 1, lambda_2533)

    def lambda_2544():

        label("loc_2544")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2544")

    QueueWorkItem2(0xF, 1, lambda_2544)
    Sleep(50)

    def lambda_255A():

        label("loc_255A")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_255A")

    QueueWorkItem2(0xA, 1, lambda_255A)

    def lambda_256B():

        label("loc_256B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_256B")

    QueueWorkItem2(0xD, 1, lambda_256B)
    Sleep(50)

    def lambda_2581():

        label("loc_2581")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2581")

    QueueWorkItem2(0xC, 1, lambda_2581)

    def lambda_2592():

        label("loc_2592")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_2592")

    QueueWorkItem2(0xE, 1, lambda_2592)
    Sleep(50)

    def lambda_25A8():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25A8)

    def lambda_25B6():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_25B6)
    Fade(250)
    OP_43(0x11, 0x1, 0x0, 0x5)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_25E0():
        OP_6D(1390, 0, 150800, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_25E0)
    ClearChrFlags(0x12, 0x80)
    OP_8E(0x12, 0xFFFFFE3E, 0x0, 0x23E38, 0xFA0, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xA, 0x1)

    ChrTalk(    #96
        0x8,
        "#097F#5P尤莉亚上尉……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x23)
    Sleep(500)

    ChrTalk(    #97
        0x12,
        (
            "#172F#4P包括王都在内的五大都市的近郊\x01",
            "全都出现了不明真身的魔兽群！\x02\x03",

            "从报告判断，\x01",
            "看来是人形兵器！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1005F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        "#1042F#5P终于出动了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        (
            "#172F#4P另外，各地的关所\x01",
            "都出现了装甲魔兽群和\x01",
            "红衣士兵！\x02\x03",

            "现在各守备队\x01",
            "正在迎击！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        "#1125F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#160F#5P看来我得尽快赶回\x01",
            "哈肯大门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        "#175F而、而且……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        "#161F#5P什么？还有？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        (
            "#178F虽然详情不明……\x01",
            "在『四轮之塔』上发生了非常事件。\x02\x03",

            "好像一股未知的『黑暗』\x01",
            "包围在塔顶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1020F#5P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "#1063F#5P哼……\x01",
            "看来我那不祥的预感成真了\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x12,
        (
            "#178F另外，巡逻中的警备艇\x01",
            "虽然试图接近调查……\x02\x03",

            "可立即陷入了机能停止状态，\x01",
            "因此不得不撤离现场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        "#160F#5P是『导力停止现象』吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        "#1122F#5P地面的侦察部队呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x12,
        "#175F应该已经被派遣过去了……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x13, 70, 0, 136750, 0)
    ClearChrFlags(0x13, 0x80)

    NpcTalk(    #112
        0x13,
        "男人的声音",
        "#1P报、报告！\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2AA4():
        OP_6D(1350, 0, 150430, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AA4)

    def lambda_2ABC():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2ABC)

    def lambda_2ACC():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2ACC)

    def lambda_2ADA():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2ADA)
    Sleep(50)

    def lambda_2AED():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2AED)

    def lambda_2AFB():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2AFB)
    Sleep(50)

    def lambda_2B0E():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B0E)

    def lambda_2B1C():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B1C)
    Sleep(50)

    def lambda_2B2F():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B2F)

    def lambda_2B3D():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B3D)

    def lambda_2B4B():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2B4B)
    OP_8E(0x13, 0xFFFFFF38, 0x0, 0x23668, 0xFA0, 0x0)

    ChrTalk(    #113
        0x13,
        (
            "#4P被派往各塔的侦察部队\x01",
            "全部被击退了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x13,
        (
            "#4P实、实在是难以置信！\x01",
            "似乎每支部队都是\x01",
            "被一个敌人给彻底打败的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x12,
        "#173F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1005F#5P难、难道……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1035F#5P嗯……\x01",
            "应该是『执行者』。\x02\x03",

            "#1042F父亲……\x01",
            "他们非普通士兵能敌。\x02\x03",

            "请让我去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C74():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C74)

    def lambda_2C82():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C82)
    Sleep(50)

    def lambda_2C95():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2C95)

    def lambda_2CA3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2CA3)
    Sleep(50)

    def lambda_2CB6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CB6)

    def lambda_2CC4():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2CC4)
    Sleep(50)

    def lambda_2CD7():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2CD7)

    def lambda_2CE5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CE5)
    Sleep(50)

    def lambda_2CF8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF8)
    TurnDirection(0x12, 0x102, 400)
    Sleep(200)

    ChrTalk(    #118
        0x11,
        "#1125F#4P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1009F#2P等等，约修亚……\x01",
            "你又想单独行动了吗。\x02\x03",

            "这么快就忘了昨天的约定？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #120
        0x102,
        "#1043F#6P艾丝蒂尔，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1006F#2P既然『结社』已经出动，\x01",
            "身为游击士也不能放任不管。\x02\x03",

            "我一定要跟你去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        "#1044F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "#020F#6P不光是艾丝蒂尔，\x01",
            "我也要和你们一起去。\x02\x03",

            "毕竟我也有些个人恩怨要了结呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xF,
        "#070F嗯，我也是。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(500)

    ChrTalk(    #125
        0x102,
        "#1044F#5P雪拉姐、金先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xD,
        (
            "#051F#6P好啦，这本来也不是\x01",
            "你一个人的事情。\x02\x03",

            "可别抢着一个人立功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xE,
        (
            "#560F#6P没、没错啊哥哥！\x02\x03",

            "#061F在这种时候，\x01",
            "才更需要大家齐心协力啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)
    Sleep(500)

    ChrTalk(    #128
        0x102,
        (
            "#1054F#5P阿加特，提妲……\x02\x03",

            "#1053F……谢谢，你们真是帮了我大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x11,
        (
            "#1125F#4P看来你们已经决定好了。\x02\x03",

            "#1122F我向游击士协会提出请求。\x02\x03",

            "拜托你们调查并解决\x01",
            "『四轮之塔』所发生的异变。\x02\x03",

            "这是来自军队的正式委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_301A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_301A)
    Sleep(500)

    ChrTalk(    #130
        0x101,
        "#1006F#5P嗯……明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#1042F#5P我们正式接受此委托。\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xC)
    OP_8C(0xC, 0, 400)
    Sleep(500)

    NpcTalk(    #132
        0xC,
        "科洛丝",
        (
            "#042F#4P……祖母大人。\x02\x03",

            "能不能把『埃尔赛尤』\x01",
            "借给我？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #133
        0x101,
        "#1004F#5P咦……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xC, 400)

    def lambda_30FC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30FC)

    def lambda_310A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_310A)

    ChrTalk(    #134
        0x12,
        "#173F#6P殿、殿下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "#094F#5P呵呵……\x01",
            "现在确实情况紧急。\x02\x03",

            "我也正准备提供\x01",
            "『埃尔赛尤』给你们……\x02\x03",

            "#090F你既然提出这个要求，\x01",
            "就是说你已经有精神准备了？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #136
        0xC,
        "科洛丝",
        (
            "#049F#4P不……还没有。\x02\x03",

            "#042F但是，当我将船归还给您的时候\x01",
            "一定会有答案的，我保证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "#090F#5P呵呵……好吧。\x02\x03",

            "#091F利贝尔的希望之翼，\x01",
            "请你们任意使用。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0xC,
        "科洛丝",
        "#048F#4P非常感谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x12, 400)
    Sleep(500)

    NpcTalk(    #139
        0xC,
        "科洛丝",
        (
            "#042F#5P尤莉亚上尉，请做出发的准备。\x02\x03",

            "我们要尽快\x01",
            "前往『四轮之塔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#171F#6P遵命！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #141
        (
            "\x07\x05就这样……\x01",
            "利贝尔迎来了『百日战役』之后未曾有过的事态。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #142
        (
            "\x07\x05为了指挥王国军的所有部队，\x01",
            "卡西乌斯和摩尔根将军各自\x01",
            "返回了雷斯顿要塞和哈肯大门……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #143
        (
            "\x07\x05艾丝蒂尔一行乘坐着『埃尔赛尤』，\x01",
            "出发前往各座塔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x98, 0x4, 0x10)
    OP_AF(0xCD, 0x98)
    Sleep(100)
    OP_28(0x99, 0x4, 0x10)
    OP_28(0x99, 0x4, 0x20)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_535 end

    def Function_5_340A(): pass

    label("Function_5_340A")

    SetChrPos(0x11, -450, 0, 149660, 0)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x800)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0xFFFFFE3E, 0x0, 0x24540, 0x3E8, 0x0)
    Return()

    # Function_5_340A end

    def Function_6_3450(): pass

    label("Function_6_3450")

    SetChrChipByIndex(0xFE, 15)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xB4, 0x0, 0x242AC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_3450 end

    def Function_7_347B(): pass

    label("Function_7_347B")

    SetChrChipByIndex(0xFE, 16)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFC68, 0x0, 0x24284, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_347B end

    def Function_8_34A6(): pass

    label("Function_8_34A6")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF560, 0x0, 0x2457C, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_8_34A6 end

    def Function_9_34C7(): pass

    label("Function_9_34C7")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF5B0, 0x0, 0x23F46, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_9_34C7 end

    def Function_10_34E8(): pass

    label("Function_10_34E8")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x8FC, 0x0, 0x24662, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_10_34E8 end

    def Function_11_3509(): pass

    label("Function_11_3509")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x398, 0x0, 0x23FA0, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_3509 end

    def Function_12_352A(): pass

    label("Function_12_352A")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x24C70, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_12_352A end

    def Function_13_354B(): pass

    label("Function_13_354B")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0x384, 0x0, 0x2446E, 0x3E8, 0x0)

    def lambda_356A():

        label("loc_356A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_356A")

    QueueWorkItem2(0xFE, 1, lambda_356A)
    Return()

    # Function_13_354B end

    def Function_14_3576(): pass

    label("Function_14_3576")

    ClearChrFlags(0xFE, 0x80)
    OP_8F(0xFE, 0xFFFFF844, 0x0, 0x24432, 0x3E8, 0x0)

    def lambda_3595():

        label("loc_3595")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3595")

    QueueWorkItem2(0xFE, 1, lambda_3595)
    Return()

    # Function_14_3576 end

    def Function_15_35A1(): pass

    label("Function_15_35A1")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(830, 0, 138280, 0)
    OP_67(0, 8039, -10000, 0)
    OP_6B(2350, 0)
    OP_6C(44000, 0)
    OP_6E(488, 0)
    OP_D2(0x70141, 0x70145, 0x12)
    OP_D2(0x6011B, 0x60120, 0x13)
    OP_D2(0x2701D4, 0x2701D9, 0x14)
    OP_D2(0x2700B0, 0x2700B4, 0x15)
    OP_D2(0x700E0, 0x700E4, 0x16)
    OP_D2(0x704AA, 0x704AE, 0x17)
    SetChrChipByIndex(0x8, 18)
    SetChrChipByIndex(0xC, 19)
    SetChrChipByIndex(0x15, 20)
    SetChrChipByIndex(0x16, 21)
    SetChrChipByIndex(0x17, 22)
    SetChrChipByIndex(0x14, 23)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -90, 0, 150140, 180)
    SetChrPos(0x14, 3790, 800, 152270, 270)
    SetChrPos(0xC, -1510, 0, 148970, 180)
    SetChrPos(0x15, 1650, 0, 148500, 180)
    SetChrPos(0x16, 560, 0, 148300, 180)
    SetChrPos(0x101, -360, 0, 145930, 0)
    SetChrPos(0x102, 790, 0, 145890, 0)
    SetChrPos(0xA, 740, 0, 144730, 0)
    SetChrPos(0xD, -800, 0, 143680, 0)
    SetChrPos(0xE, -1250, 0, 144610, 0)
    SetChrPos(0xF, 1230, 0, 143850, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(1000, 0)

    def lambda_3754():
        OP_6D(290, 0, 147230, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3754)

    def lambda_376C():
        OP_67(0, 7500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_376C)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(1500, 0, 147770, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(44000, 0)
    OP_6E(433, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #144
        0x15,
        (
            "#700F#5P就像我前面所说，\x01",
            "这都是卡西乌斯准将的指示。\x02\x03",

            "他事先就知道了\x01",
            "王都会迎来危机。\x02\x03",

            "#703F所以，想到以导力兵器为主武器的\x01",
            "正规军是守不住的……\x02\x03",

            "#701F就决定投入白刃战经验\x01",
            "丰富的特务兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x16,
        (
            "#115F#5P当然，必须要有一个理由\x01",
            "来让服刑中的我们投入战斗。\x02\x03",

            "#111F所以故意让我们在被\x01",
            "押往王城的途中卷入这次骚乱，\x01",
            "结果成功保卫了城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1007F#6P原，原来如此……\x02\x03",

            "#1019F虽然我怎么想都\x01",
            "觉得说不通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#1040F好像陛下你们\x01",
            "是知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#090F#5P嗯，关于这件事\x01",
            "卡西乌斯先生事先跟我说过。\x02\x03",

            "虽然接下来可能会有很多\x01",
            "批判的声音，\x01",
            "但是，国民的安全是无可替代的。\x02\x03",

            "#091F最重要的是，我相信\x01",
            "理查德先生的爱国心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x16,
        "#115F#6P……您太抬举我了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1006F#6P是吗，这样的话……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #151
        0x101,
        (
            "#1015F#6P这么说起来……\x02\x03",

            "叫我们来王城也\x01",
            "和此事有关？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#094F#5P嗯，也有这层因素……\x02\x03",

            "#090F其实我有一些关于\x01",
            "科洛蒂娅的事想跟你们说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        "#1044F……关于科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xC,
        (
            "#406F#5P嗯，其实……\x02\x03",

            "#400F今早已经为我举办了\x01",
            "一个继承王位的简单仪式。\x02\x03",

            "如今我的身份已经是\x01",
            "利贝尔王国的下一任女王了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #156
        0x101,
        "#1004F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xE,
        "#560F哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        "#1040F……你终于下了决心啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D47")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过学院解放的任务】\x01",        # 0
            "【◇没完成过学院解放的任务】\x01",      # 1
            "【◇不变更】\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D3B"),
        (1, "loc_3D41"),
        (SWITCH_DEFAULT, "loc_3D47"),
    )


    label("loc_3D3B")

    OP_A2(0x202F)
    Jump("loc_3D47")

    label("loc_3D41")

    OP_A3(0x202F)
    Jump("loc_3D47")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3EC8")

    ChrTalk(    #159
        0xC,
        (
            "#466F#5P哪里……\x01",
            "只是任性妄为而已。\x02\x03",

            "#405F艾丝蒂尔，约修亚。\x01",
            "还有大家……\x02\x03",

            "听说你们救了\x01",
            "学院的各位？\x02\x03",

            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1016F#6P啊……嗯。\x02\x03",

            "#1006F不过不光是我们\x01",
            "的功劳哦，\x02\x03",

            "亚妮拉丝和\x01",
            "基库也有帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        "#311F#6P啾⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xC,
        (
            "#401F#5P呵呵，好像是的。\x02\x03",

            "#406F听说发生了事件之后……\x01",
            "我认真地考虑了\x01",
            "自己究竟能做些什么。\x02\x03",

            "为了保护那些我所珍爱的人，\x01",
            "自己究竟能起到什么作用……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F6B")

    label("loc_3EC8")


    ChrTalk(    #163
        0xC,
        (
            "#405F#5P哪里……\x01",
            "只是任性妄为而已。\x02\x03",

            "#406F王国全境都陷入了混乱……\x01",
            "我认真地考虑了\x01",
            "自己究竟能做些什么。\x02\x03",

            "为了保护那些我所珍爱的人，\x01",
            "自己究竟能起到什么作用……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F6B")


    ChrTalk(    #164
        0x102,
        (
            "#1040F答案就是……\x01",
            "由自己来继承王位吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xC,
        (
            "#400F#5P是的。\x02\x03",

            "#406F对稚嫩的我来说，还没有\x01",
            "自信来背负整个王国的重任。\x02\x03",

            "尽管如此，如果能通过继承王位\x01",
            "来保护自己所珍爱的人们……\x02\x03",

            "并且保卫王国的话……\x01",
            "无论怎样的结果我也会面对。\x02\x03",

            "#401F──这就是我的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1017F#6P是吗……\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_408B():
        OP_6D(-40, 0, 149310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408B)

    def lambda_40A3():

        label("loc_40A3")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40A3")

    QueueWorkItem2(0x8, 2, lambda_40A3)

    def lambda_40B4():

        label("loc_40B4")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40B4")

    QueueWorkItem2(0x15, 2, lambda_40B4)

    def lambda_40C5():

        label("loc_40C5")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40C5")

    QueueWorkItem2(0x16, 2, lambda_40C5)

    def lambda_40D6():

        label("loc_40D6")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40D6")

    QueueWorkItem2(0x102, 2, lambda_40D6)

    def lambda_40E7():

        label("loc_40E7")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40E7")

    QueueWorkItem2(0xA, 2, lambda_40E7)

    def lambda_40F8():

        label("loc_40F8")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40F8")

    QueueWorkItem2(0xD, 2, lambda_40F8)

    def lambda_4109():

        label("loc_4109")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4109")

    QueueWorkItem2(0xE, 2, lambda_4109)

    def lambda_411A():

        label("loc_411A")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_411A")

    QueueWorkItem2(0xF, 2, lambda_411A)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xFFFFFABA, 0x0, 0x2437E, 0x5DC, 0x0)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 16)
    SetChrFlags(0x101, 0x2)

    def lambda_4167():
        OP_99(0x101, 0x10, 0x13, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4167)
    OP_99(0xC, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #167
        0x101,
        (
            "#1001F#6P科洛丝，恭喜你！\x02\x03",

            "#1018F你终于找到属于\x01",
            "自己的路了！\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x4, 0x5, 0x5DC)
    Sleep(500)

    ChrTalk(    #168
        0xC,
        "#406F#5P艾丝蒂尔……谢谢你。\x02",
    )

    CloseMessageWindow()
    OP_99(0xC, 0x5, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #169
        0xC,
        (
            "#405F#5P不过，我还不够成熟，\x01",
            "也不知道自己能做些什么。\x02\x03",

            "当我感到为难的时候……\x01",
            "能不能请你们帮忙？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1001F#6P哈哈！\x01",
            "这还用说吗！\x02\x03",

            "#1008F再说我们自身\x01",
            "也一样不成熟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#1049F就像你一直以来\x01",
            "对我们的帮助一样……\x02\x03",

            "#1041F在必要时我们随时会帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xC,
        (
            "#409F#5P艾丝蒂尔，约修亚……\x02\x03",

            "#401F……真的很谢谢你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x2)
    OP_44(0x15, 0x2)
    OP_44(0x16, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xA, 0x2)
    OP_44(0xD, 0x2)
    OP_44(0xE, 0x2)
    OP_44(0xF, 0x2)
    OP_6D(910, 0, 149260, 1200)

    ChrTalk(    #173
        0x16,
        (
            "#115F#5P（……如今我才真正认识到…\x01",
            "当初的自己有多么愚蠢。)\x02\x03",

            "#116F（根本没看清这些担负着未来的\x01",
            "年轻人所具备的可能性，\x01",
            "而做出了那样的蠢事……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x15,
        "#700F#2P（理查德先生……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(300)

    ChrTalk(    #175
        0x8,
        (
            "#091F#5P（呵呵，这叫什么话。）\x02\x03",

            "#090F（你自己也是担负着\x01",
            "王国未来的年轻人啊。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x15,
        "#701F#2P（陛下……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x16,
        "#118F#2P（您、您开玩笑了……）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x17, 10, 0, 137650, 0)
    ClearChrFlags(0x17, 0x80)

    NpcTalk(    #178
        0x17,
        "青年的声音",
        "#4S#1P报、报告！\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xF, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_45C5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45C5)

    def lambda_45D3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_45D3)
    Sleep(50)

    def lambda_45E6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_45E6)

    def lambda_45F4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_45F4)
    Sleep(50)

    def lambda_4607():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4607)

    def lambda_4615():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4615)
    Sleep(50)

    def lambda_4628():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4628)

    def lambda_4636():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4636)
    SetChrChipByIndex(0xC, 19)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x800)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x800)

    def lambda_466C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_466C)

    def lambda_467A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_467A)

    def lambda_4688():
        OP_6D(1100, 0, 146260, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4688)

    def lambda_46A0():
        OP_67(0, 5630, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_46A0)

    def lambda_46B8():
        OP_6B(1900, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_46B8)

    def lambda_46C8():
        OP_6E(488, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_46C8)
    Sleep(1000)

    def lambda_46DD():
        OP_8E(0xFE, 0x154, 0x0, 0x229D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_46DD)
    Sleep(1000)

    def lambda_46FD():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x23A0A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46FD)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #179
        0x15,
        (
            "#702F#5P什么事？\x01",
            "市区又发生了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x17,
        (
            "#2P不、不是，那边的\x01",
            "局势已经勉强收拾住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x17,
        (
            "#2P猎兵们也都从\x01",
            "王都撤退了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        "#700F#5P那么是什么事？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(100)
    OP_1D(0x23)
    Sleep(500)

    ChrTalk(    #183
        0x17,
        (
            "#2P刚、刚才收到了\x01",
            "哈肯大门的联络……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x17,
        (
            "#2P说帝国军开始在边境\x01",
            "附近集结了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x101,
        "#1020F#5P#4S啊！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #186
        0x16,
        "#117F#5P果然来了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#092F#5P……集结的\x01",
            "规模怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x17,
        (
            "#2P现在有一个师\x01",
            "左右的兵力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x17,
        (
            "#2P不、不过其中似乎有\x01",
            "坦克部队……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x15,
        "#704F#5P你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        (
            "#055F#5P等、等等！\x02\x03",

            "在导力停止现象下\x01",
            "为什么坦克能够开动！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xA,
        (
            "#024F#5P难道他们使用了和\x01",
            "『结社』相同的技术！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x17,
        (
            "#2P不……他们使用的似乎是\x01",
            "使用了不搭载导力机械的型号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x17,
        (
            "#2P据观察，是\x01",
            "由『蒸气机』驱动的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1026F#5P蒸气……机？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 400)
    Sleep(300)

    ChrTalk(    #196
        0xE,
        (
            "#065F#6P那个那个……\x01",
            "是比内燃引擎还要原始的\x01",
            "使用蒸气能量的引擎……\x02\x03",

            "随着导力器的普及，\x01",
            "这种发明很快就被弃用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x16,
        (
            "#112F#5P……应该不可能有哪个国家\x01",
            "还拥有以它为动力的坦克。\x02\x03",

            "因为与导力坦克的成本\x01",
            "和性能相比，实在是太没价值了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CD8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4CD8)

    ChrTalk(    #198
        0xF,
        (
            "#074F#5P那只有一种可能性了……\x02\x03",

            "#072F这是偷偷地在帝国\x01",
            "内部制造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1002F#5P就、就是说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x15,
        (
            "#703F#5P……他们早就预计到\x01",
            "这种情况了吗？\x02\x03",

            "#702F那么结社那伙儿人\x01",
            "所说的『下一次试练』……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DAA():
        OP_6D(1100, 0, 147600, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DAA)

    def lambda_4DC2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DC2)
    Sleep(50)

    def lambda_4DD5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DD5)

    def lambda_4DE3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DE3)
    Sleep(50)

    def lambda_4DF6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4DF6)

    def lambda_4E04():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4E04)
    Sleep(50)

    def lambda_4E17():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4E17)

    def lambda_4E25():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4E25)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #201
        0x102,
        (
            "#1043F#4P嗯……\x01",
            "恐怕就是指这个。\x02\x03",

            "#1042F而且他们这次是\x01",
            "把王都当作人质了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x16,
        (
            "#118F#5P『只要想的话\x01",
            "随时可以攻击王都』……\x02\x03",

            "也有这种意图在里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x102,
        (
            "#1035F#4P还有一点……\x02\x03",

            "#1042F父亲应该是把您\x01",
            "当作了隐藏的牌。\x02\x03",

            "在发生紧急情况时\x01",
            "可以代替自己\x01",
            "进行派遣的王牌。\x02\x03",

            "可是现在这张牌已经\x01",
            "使用过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x16,
        "#113F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x15,
        (
            "#703F#5P『噬身之蛇』……\x01",
            "竟算计得这么深。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xC)
    Sleep(500)
    TurnDirection(0xC, 0x8, 400)

    ChrTalk(    #206
        0xC,
        (
            "#402F#6P……祖母大人。\x02\x03",

            "请派我前往\x01",
            "哈肯大门。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_50D9():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50D9)

    def lambda_50E7():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_50E7)
    Sleep(50)

    def lambda_50FA():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_50FA)

    def lambda_5108():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5108)
    Sleep(50)

    def lambda_511B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_511B)

    def lambda_5129():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5129)

    ChrTalk(    #207
        0x101,
        "#1004F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        "#1044F#4P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xC,
        (
            "#406F#6P如果我什么也不做，\x01",
            "怎么对得起为了让我们逃走\x01",
            "而受伤的叔叔呢。\x02\x03",

            "#402F我一定要作为祖母大人的代理人\x01",
            "去完成和帝国军的交涉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#094F#5P……明白了。\x02\x03",

            "#092F虽然互不侵犯条约已经缔结，\x01",
            "不过王国和帝国之间的天平\x01",
            "至今还不稳定。\x02\x03",

            "这次的事件有可能会\x01",
            "招致更大的动荡。\x02\x03",

            "#090F恢复天平的平衡……\x01",
            "这件事就拜托给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xC,
        "#401F#6P……是！\x02",
    )

    CloseMessageWindow()

    def lambda_52B7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52B7)
    Sleep(80)

    def lambda_52CA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_52CA)
    Sleep(80)

    def lambda_52DD():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_52DD)
    Sleep(80)

    def lambda_52F0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_52F0)
    Sleep(80)

    def lambda_5303():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5303)
    Sleep(80)

    def lambda_5316():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5316)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        "\x07\x05艾丝蒂尔她们互相交换了眼神。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    def lambda_5366():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5366)
    Sleep(50)

    def lambda_5379():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5379)
    Sleep(50)

    def lambda_538C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_538C)
    Sleep(50)

    def lambda_539F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_539F)
    Sleep(50)

    def lambda_53B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_53B2)
    Sleep(50)

    def lambda_53C5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_53C5)
    Sleep(500)

    ChrTalk(    #213
        0x101,
        (
            "#1006F#6P我说……\x02\x03",

            "那我们也一起\x01",
            "去，行吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5464():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5464)
    Sleep(50)

    def lambda_5477():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5477)
    Sleep(50)

    def lambda_548A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_548A)
    Sleep(50)
    OP_8C(0x15, 180, 400)

    ChrTalk(    #214
        0xC,
        "#409F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        (
            "#1040F#4P我们会护送公主殿下\x01",
            "平安到达哈肯大门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xD,
        (
            "#051F#6P并且，万一\x01",
            "战争一触即发，我们\x01",
            "也会起到自己的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "#027F当然，根据协会的规定，\x01",
            "我们不能参与战争……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xF,
        (
            "#071F不过站在中立立场上的仲裁，\x01",
            "我们会尽力而为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        "#405F#5P各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x8,
        (
            "#090F#5P呵呵……\x01",
            "这真是求之不得。\x02\x03",

            "#091F拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#1006F#6P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        "#1040F#4P请交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x16,
        (
            "#115F#5P……艾丝蒂尔，约修亚。\x02\x03",

            "#110F关于『结社』的动向\x01",
            "就让我们来负责监控吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x15,
        (
            "#701F#5P我们会准备好万全的对策，\x01",
            "即使那架巨大机器人出现在\x01",
            "王都，我们也会积极应对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1025F#6P二位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#1035F#4P拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05就这样，艾丝蒂尔她们\x01",
            "护送着科洛丝前往哈肯大门了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #228
        (
            "\x07\x05在穿过了格鲁纳门，以尽可能\x01",
            "快的速度通过了洛连特地区后……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #229
        "\x07\x05艾丝蒂尔她们终于抵达了哈肯大门。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    ClearChrFlags(0x101, 0x40)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_35A1 end

    SaveToFile()

Try(main)
