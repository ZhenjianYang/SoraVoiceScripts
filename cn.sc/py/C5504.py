from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5504   ._SN',
        MapName             = 'Other',
        Location            = 'C5504.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        '亚妮拉丝的头',                         # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH12180 ._CH',             # 00
        'ED6_DT29/CH12181 ._CH',             # 01
        'ED6_DT29/CH12230 ._CH',             # 02
        'ED6_DT29/CH12231 ._CH',             # 03
        'ED6_DT29/CH12270 ._CH',             # 04
        'ED6_DT29/CH12271 ._CH',             # 05
        'ED6_DT29/CH12360 ._CH',             # 06
        'ED6_DT29/CH12361 ._CH',             # 07
        'ED6_DT26/CH20268 ._CH',             # 08
        'ED6_DT26/CH20266 ._CH',             # 09
        'ED6_DT27/CH03005 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT29/CH12180P._CP',             # 00
        'ED6_DT29/CH12181P._CP',             # 01
        'ED6_DT29/CH12230P._CP',             # 02
        'ED6_DT29/CH12231P._CP',             # 03
        'ED6_DT29/CH12270P._CP',             # 04
        'ED6_DT29/CH12271P._CP',             # 05
        'ED6_DT29/CH12360P._CP',             # 06
        'ED6_DT29/CH12361P._CP',             # 07
        'ED6_DT26/CH20268P._CP',             # 08
        'ED6_DT26/CH20266P._CP',             # 09
        'ED6_DT27/CH03005P._CP',             # 0A
    )

    DeclNpc(
        X                   = -19520,
        Z                   = -200,
        Y                   = -19050,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1F8,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -8610,
        Z                   = 0,
        Y                   = 35650,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 890,
        Z                   = 0,
        Y                   = 17280,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24590,
        Z                   = 0,
        Y                   = 17330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 19740,
        Z                   = 0,
        Y                   = 29560,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16170,
        Z                   = 0,
        Y                   = 8880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 24590,
        TriggerZ            = 0,
        TriggerY            = 35090,
        TriggerRange        = 1000,
        ActorX              = 25030,
        ActorZ              = 0,
        ActorY              = 35520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28980,
        TriggerZ            = 0,
        TriggerY            = -18140,
        TriggerRange        = 800,
        ActorX              = -28980,
        ActorZ              = 1000,
        ActorY              = -18140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_341",          # 03, 3
        "Function_4_404",          # 04, 4
        "Function_5_12D2",         # 05, 5
        "Function_6_12E6",         # 06, 6
        "Function_7_1522",         # 07, 7
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_20B")

    Return()

    # Function_0_1F6 end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E")
    OP_6F(0x0, 0)
    Jump("loc_225")

    label("loc_21E")

    OP_6F(0x0, 60)

    label("loc_225")

    Return()

    # Function_1_20C end

    def Function_2_226(): pass

    label("Function_2_226")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x104, 1)"), scpexpr(EXPR_END)), "loc_295")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x04\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1120)
    Jump("loc_2FB")

    label("loc_295")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x04\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x04\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2FB")

    Jump("loc_32F")

    label("loc_2FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_32F")

    Sleep(30)
    Call(0, 3)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_226 end

    def Function_3_341(): pass

    label("Function_3_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403")

    ChrTalk(    #3
        0x101,
        (
            "#1004F啊……！\x02\x03",

            "难不成，这个\x01",
            "就是我们的装备？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        (
            "#811F嗯，似乎是呢⊙\x02\x03",

            "#1310F说不定其它装备\x01",
            "也被藏在什么地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1006F嗯～\x01",
            "虽然想避开和魔兽的战斗，\x01",
            "但似乎值得探索一下呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    label("loc_403")

    Return()

    # Function_3_341 end

    def Function_4_404(): pass

    label("Function_4_404")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_3F(0x9, 1)
    OP_3F(0x104, 1)
    OP_3F(0x125, 1)
    OP_3F(0xCF, 1)
    OP_3F(0x104, 1)
    OP_3F(0x125, 1)
    OP_6D(-19290, 0, -16309, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18710, 0, -16030, 268)
    SetChrPos(0x10A, -19980, 0, -19410, 243)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x10A, 9)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x10A, 0x1)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)

    ChrTalk(    #6
        0x101,
        (
            "#5P#1007F嗯……\x02\x03",

            "#1003F……已经早上了吗……\x02\x03",

            "……………………………\x02\x03",

            "#1020F！！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(1000, 0)
    OP_0D()
    OP_99(0x101, 0x0, 0x2, 0x1F4)
    Sleep(500)
    SetChrSubChip(0x101, 5)
    Sleep(200)
    SetChrSubChip(0x101, 2)
    Sleep(200)
    SetChrSubChip(0x101, 5)
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        (
            "#5P#1020F咦……\x02\x03",

            "这里，是哪里……？\x02\x03",

            "记得被敌人袭击之后……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 5)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(800)
    SetChrSubChip(0x101, 5)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    Sleep(500)
    SetChrSubChip(0x101, 4)
    Sleep(200)
    SetChrSubChip(0x101, 7)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 180, 0)
    OP_0D()
    Sleep(500)
    OP_8E(0x101, 0xFFFFB776, 0x0, 0xFFFFB79E, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x101,
        (
            "#5P#1002F亚妮拉丝！\x02\x03",

            "快起来，亚妮拉丝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#1311F#6P嗯……嘿嘿……\x02\x03",

            "兔子和……\x01",
            "熊的娃娃……\x02\x03",

            "……要选哪一个呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#5P#1007F在、在做什么梦啊……\x02\x03",

            "#1005F亚妮拉丝！\x01",
            "不得了啦，快起来啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        "#1316F#6P嗯～……？\x02",
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x0, 0x2, 0x3E8)
    OP_99(0x10A, 0x2, 0x0, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0x0, 0x3, 0x3E8)

    ChrTalk(    #12
        0x10A,
        (
            "#1314F#6P咦，艾丝蒂尔……\x02\x03",

            "啊，对了……\x01",
            "已经是晨练的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#5P#1007F败给你了……\x01",
            "现在不是晨练的时候啦。\x02\x03",

            "#1014F拜托你快醒来啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#813F#6P咦……？\x02",
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    OP_99(0x10A, 0x0, 0x3, 0x3E8)
    ClearChrFlags(0x8, 0x80)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    SetChrFlags(0x8, 0x80)
    OP_99(0x10A, 0x3, 0x7, 0x3E8)
    Sleep(1000)
    OP_99(0x10A, 0x7, 0x9, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0x9, 0xD, 0x3E8)
    Sleep(500)
    OP_99(0x10A, 0xD, 0x13, 0x3E8)
    OP_99(0x10A, 0x10, 0x13, 0x3E8)

    ChrTalk(    #15
        0x10A,
        (
            "#814F#6P…………………………\x02\x03",

            "……嗯～\x01",
            "怎么回事？\x02\x03",

            "难道说，\x01",
            "昨天的袭击只是一场梦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#5P#1007F我也希望是这样。\x02\x03",

            "但既然我们两人都记得，\x01",
            "应该不可能是梦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x10A, 0x7, 0x9, 0x3E8)

    ChrTalk(    #17
        0x10A,
        (
            "#819F#6P啊～原来如此啊～\x02\x03",

            "呀～这次姐姐\x01",
            "可真是败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#5P#1019F亚妮拉丝……\x01",
            "还在犯迷糊啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x10A, 0x2)
    SetChrFlags(0x10A, 0x1)
    SetChrPos(0x101, -20730, 0, -19460, 68)
    SetChrPos(0x10A, -19800, 0, -18290, 159)
    ClearMapFlags(0x1)
    OP_6D(-24650, 0, -20010, 0)
    OP_67(0, 12770, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(179000, 0)
    OP_6E(262, 0)
    OP_1D(0x15)
    OP_C8(0x200, 0x46, "C_PLAC02._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_A3F():
        OP_6D(-19150, 0, -18900, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_A3F)

    def lambda_A57():
        OP_67(0, 12770, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A57)

    def lambda_A6F():
        OP_6C(15000, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_A6F)

    def lambda_A7F():
        OP_8C(0x101, 190, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A7F)

    def lambda_A8D():
        OP_8C(0x10A, 90, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8D)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    Sleep(100)

    def lambda_AAA():
        OP_8C(0x101, 245, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AAA)

    def lambda_AB8():
        OP_8C(0x10A, 92, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB8)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    Fade(1000)
    OP_6D(-21320, 0, -19030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_8C(0x10A, 172, 500)
    Sleep(100)
    OP_8C(0x101, 102, 500)
    Sleep(500)

    ChrTalk(    #19
        0x10A,
        (
            "#817F#2P嗯，首先\x01",
            "试着把状况汇总一下吧。\x02\x03",

            "#812F昨天夜里，貌似猎兵团的集团\x01",
            "袭击了宿舍……\x02\x03",

            "克鲁茨前辈受了伤，\x01",
            "在我们急忙赶到后，\x01",
            "敌人就紧接着从窗户闯入……\x02\x03",

            "然后我们两个\x01",
            "马上被弄昏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F#5P嗯。\x01",
            "和我的记忆一样。\x02\x03",

            "问题是，怎么会在这种地方\x01",
            "醒过来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        (
            "#812F#2P嗯，确实很奇怪。\x02\x03",

            "携带品之类的\x01",
            "倒是没遗失的样子……\x02\x03",

            "不过昨晚身上穿戴的\x01",
            "武具好像都被卸下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1004F#5P我、我也是。\x02\x03",

            "#1015F这么说来，把我们\x01",
            "搬来这里的是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x18\x07\x05把艾丝蒂尔她们搬到森林的是？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【克鲁茨】\x01",                # 0
            "【来袭的猎兵团】\x01",          # 1
            "【除此以外的第三者】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DA5"),
        (1, "loc_EC7"),
        (2, "loc_F3D"),
        (SWITCH_DEFAULT, "loc_FCB"),
    )


    label("loc_DA5")


    ChrTalk(    #24
        0x10A,
        (
            "#813F#2P……这个可能性应该很低。\x02\x03",

            "就算是前辈，在那种状况下\x01",
            "也不可能搬得动我们两个人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1003F#5P的确……\x02\x03",

            "而且如果是克鲁茨前辈的话，\x01",
            "就不会夺取我们的装备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10A,
        (
            "#812F#2P最有可能的\x01",
            "是来袭的猎兵团……\x02\x03",

            "但如果是这样，不把我们捆起来，\x01",
            "而是就这么丢在这里的理由就很不符合逻辑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCB")

    label("loc_EC7")

    OP_2B(0x7E, 0x3)

    ChrTalk(    #27
        0x10A,
        (
            "#812F#2P嗯……\x01",
            "虽然一般都会这么想……\x02\x03",

            "但是，不把我们捆起来，\x01",
            "而是就这么丢在这里的理由就很不符合逻辑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCB")

    label("loc_F3D")


    ChrTalk(    #28
        0x10A,
        (
            "#1316F#2P嗯……\x01",
            "倒也不是不可能。\x02\x03",

            "#812F最有可能的\x01",
            "是来袭的猎兵团。\x02\x03",

            "只是，不把我们捆起来，\x01",
            "而是就这么丢在这里的理由就很不符合逻辑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCB")

    label("loc_FCB")


    ChrTalk(    #29
        0x101,
        (
            "#1002F#5P把昏倒的我们\x01",
            "运来这里并解除武装之后……\x02\x03",

            "或许发生了什么意外，\x01",
            "急忙转移到别的地方了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10A,
        (
            "#816F#2P原来如此。\x01",
            "这或许很有可能。\x02\x03",

            "若是这样，在这里久留\x01",
            "似乎也很危险。\x02\x03",

            "艾丝蒂尔，你带了地图吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1004F#5P啊，嗯。\x01",
            "因为行李没被拿走……\x02\x03",

            "#1006F……有了有了。\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x2400A0, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #32
        (
            "\x07\x00#810F嗯，果然没错。\x02\x03",

            "这里就是昨天用来训练的\x01",
            "『圣科洛瓦森林』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 340, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #33
        (
            "\x07\x00#1015F这么说……\x02\x03",

            "当前的目的就是要逃出森林，\x01",
            "并确认宿舍的情况吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #34
        (
            "\x07\x00#813F嗯，虽然也很在意\x01",
            "前辈的安危等一些事情……\x02\x03",

            "但首先必须要打破现状才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    OP_AE(0x3E8)
    Sleep(1000)

    ChrTalk(    #35
        0x10A,
        (
            "#810F#2P那么，出发吧。\x02\x03",

            "我们几乎是赤手空拳，\x01",
            "所以最好小心谨慎地行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1002F#5P嗯，知道了。\x02\x03",

            "要是能设法取回\x01",
            "被卸下的装备就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100D)
    OP_28(0x7F, 0x1, 0x2)
    OP_28(0x7F, 0x1, 0x4)
    OP_28(0x7F, 0x1, 0x8)
    OP_28(0x7F, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_4_404 end

    def Function_5_12D2(): pass

    label("Function_5_12D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1")
    Call(0, 6)
    Jump("loc_12E5")

    label("loc_12E1")

    Call(0, 7)

    label("loc_12E5")

    Return()

    # Function_5_12D2 end

    def Function_6_12E6(): pass

    label("Function_6_12E6")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-28980, 0, -18140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -27880, 0, -18520, 325)
    SetChrPos(0x10A, -28610, 0, -19090, 350)
    OP_0D()

    ChrTalk(    #37
        0x101,
        (
            "#1002F这个果然\x01",
            "是猎兵团使用过的帐篷吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#812F可能性很高的样子。\x02\x03",

            "总之先调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #39
        "\x07\x00得到5个\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1F6, 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #40
        "\x07\x00得到2个\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1FE, 2)

    ChrTalk(    #41
        0x101,
        (
            "#1007F嗯……\x01",
            "除此之外没有别的东西了。\x02\x03",

            "#1015F要是我们的\x01",
            "装备在就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#1316F看来没那么简单呢。\x02\x03",

            "#810F不过，帐篷的状况很不错，\x01",
            "或许可以用来休息。\x02\x03",

            "虽然没多少空闲时间，\x01",
            "但要是累了就回来这里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1011F嗯，明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x100E)
    EventEnd(0x0)
    Return()

    # Function_6_12E6 end

    def Function_7_1522(): pass

    label("Function_7_1522")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【稍微休息一下】\x01",      # 0
            "【不休息】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1650")
    OP_1F(0x0, 0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    OP_6D(-28380, 0, -18660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -28380, 0, -18660, 112)
    SetChrPos(0x10A, -28380, 0, -18660, 112)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05ＨＰ和ＥＰ恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1F(0x64, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_1652")

    label("loc_1650")

    EventEnd(0x1)

    label("loc_1652")

    Return()

    # Function_7_1522 end

    SaveToFile()

Try(main)
