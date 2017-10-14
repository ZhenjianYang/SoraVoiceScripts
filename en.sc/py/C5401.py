from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5401   ._SN',
        MapName             = 'Other',
        Location            = 'C5401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'Professor Weissmann',                  # 9
        'Loewe',                                # 10
        'Bleublanc',                            # 11
        'Walter',                               # 12
        'Luciola',                              # 13
        'Campanella',                           # 14
        'Renne',                                # 15
        'Enhanced Jaeger',                      # 16
        'Enhanced Jaeger',                      # 17
        'Afterimage',                           # 18
        'Afterimage',                           # 19
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
        'ED6_DT26/CH20383 ._CH',             # 00
        'ED6_DT27/CH03550 ._CH',             # 01
        'ED6_DT27/CH04547 ._CH',             # 02
        'ED6_DT27/CH04548 ._CH',             # 03
        'ED6_DT27/CH03530 ._CH',             # 04
        'ED6_DT27/CH03500 ._CH',             # 05
        'ED6_DT27/CH03520 ._CH',             # 06
        'ED6_DT27/CH03600 ._CH',             # 07
        'ED6_DT27/CH03510 ._CH',             # 08
        'ED6_DT27/CH04000 ._CH',             # 09
        'ED6_DT27/CH04001 ._CH',             # 0A
        'ED6_DT27/CH04003 ._CH',             # 0B
        'ED6_DT27/CH04004 ._CH',             # 0C
        'ED6_DT26/CH20208 ._CH',             # 0D
        'ED6_DT27/CH03540 ._CH',             # 0E
        'ED6_DT27/CH04620 ._CH',             # 0F
        'ED6_DT26/CH20237 ._CH',             # 10
        'ED6_DT26/CH20280 ._CH',             # 11
        'ED6_DT26/CH20305 ._CH',             # 12
        'ED6_DT26/CH20439 ._CH',             # 13
        'ED6_DT27/CH04002 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT26/CH20383P._CP',             # 00
        'ED6_DT27/CH03550P._CP',             # 01
        'ED6_DT27/CH04547P._CP',             # 02
        'ED6_DT27/CH04548P._CP',             # 03
        'ED6_DT27/CH03530P._CP',             # 04
        'ED6_DT27/CH03500P._CP',             # 05
        'ED6_DT27/CH03520P._CP',             # 06
        'ED6_DT27/CH03600P._CP',             # 07
        'ED6_DT27/CH03510P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04001P._CP',             # 0A
        'ED6_DT27/CH04003P._CP',             # 0B
        'ED6_DT27/CH04004P._CP',             # 0C
        'ED6_DT26/CH20208P._CP',             # 0D
        'ED6_DT27/CH03540P._CP',             # 0E
        'ED6_DT27/CH04620P._CP',             # 0F
        'ED6_DT26/CH20237P._CP',             # 10
        'ED6_DT26/CH20280P._CP',             # 11
        'ED6_DT26/CH20305P._CP',             # 12
        'ED6_DT26/CH20439P._CP',             # 13
        'ED6_DT27/CH04002P._CP',             # 14
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2DD",          # 01, 1
        "Function_2_2FC",          # 02, 2
        "Function_3_31D6",         # 03, 3
        "Function_4_31F3",         # 04, 4
        "Function_5_326A",         # 05, 5
        "Function_6_3348",         # 06, 6
        "Function_7_3393",         # 07, 7
        "Function_8_33EF",         # 08, 8
        "Function_9_34B0",         # 09, 9
        "Function_10_3571",        # 0A, 10
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2C3")
    OP_A3(0x10F0)
    Event(0, 10)
    Jump("loc_2DC")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_2DC")

    Return()

    # Function_0_2B2 end

    def Function_1_2DD(): pass

    label("Function_1_2DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FB")

    Return()

    # Function_1_2DD end

    def Function_2_2FC(): pass

    label("Function_2_2FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrPos(0x101, -960, 0, 45690, 0)
    SetChrPos(0x8, -1000, 1600, 89800, 0)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    def lambda_33B():

        label("loc_33B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_33B")

    QueueWorkItem2(0x8, 0, lambda_33B)
    OP_6D(-740, 0, 50090, 0)
    OP_67(0, 13680, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(410, 0)
    OP_1F(0x64, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_39A():
        OP_6D(1180, 1500, 94610, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39A)

    def lambda_3B2():
        OP_67(0, 16910, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B2)

    def lambda_3CA():
        OP_6B(2900, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CA)

    def lambda_3DA():
        OP_6C(45000, 9000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3DA)

    def lambda_3EA():
        OP_6E(550, 9000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3EA)

    def lambda_3FA():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xF848, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FA)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    Sleep(1000)

    def lambda_423():
        OP_6D(-350, 1500, 90480, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_423)

    def lambda_43B():
        OP_67(0, 5350, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43B)

    def lambda_453():
        OP_6B(2020, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_453)

    def lambda_463():
        OP_6C(57000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_463)

    def lambda_473():
        OP_6E(512, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_473)
    WaitChrThread(0x101, 0x0)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    SetChrPos(0x101, -900, 0, 78060, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_6B(1600, 6000)
    Sleep(1000)
    OP_20(0x7D0)
    OP_21()
    OP_44(0x8, 0x0)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #0
        0x8,
        "#1154F#6PWelcome aboard the Glorious.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 1)
    SetChrPos(0x8, -2000, 1500, 89380, 0)
    OP_0D()
    OP_1D(0x70)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #1
        0x8,
        (
            "#1151F#1PIt's been some time since we last met,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-1380, 1600, 84070, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(33000, 0)
    OP_6E(545, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#1002FAh, 'Professor Alba.' I thought it was you.\x02\x03",

            "I'd finally remembered when I heard\x01",
            "your voice a minute ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1154F#3PCassius Bright's daughter continues\x01",
            "to impress.\x02\x03",

            "#1150FThe seal on your memory wasn't particularly\x01",
            "strong, but throwing it off on your own is still\x01",
            "worth some manner of praise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1002F...\x02",
    )

    CloseMessageWindow()

    def lambda_702():
        OP_8F(0x8, 0xFFFFFC7C, 0x5DC, 0x14FBE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_702)
    Sleep(1000)
    Fade(500)
    OP_72(0x4, 0x4)
    OP_79(0x9, 0x1)
    OP_7B()
    OP_6D(-900, 0, 88050, 0)
    OP_67(0, 3050, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    OP_6D(-960, 0, 88610, 0)
    OP_67(0, 2550, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    WaitChrThread(0x8, 0x3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x8,
        (
            "#1150F#6PMy apologies. I've yet to properly introduce\x01",
            "myself. My true name is Georg Weissmann.\x02\x03",

            "I am one of the Anguis, supervisors of\x01",
            "the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1002F#5PAn 'Anguis'? So you're, like, one of\x01",
            "the high commanders of the society?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#1154F#6PMmm. Something like that.\x02\x03",

            "#1150FNow, as I said before, I am completely\x01",
            "prepared to answer any questions you\x01",
            "may have.\x02\x03",

            "What would you like to ask first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1003F#5P...\x02\x03",

            "#1007FHonestly, there's so much to ask.\x01",
            "I'm not even sure where to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1151F#6PYou needn't fret. Take your time thinking\x01",
            "things over.\x02\x03",

            "If it pleases you, I could play a relaxing\x01",
            "etude while you collect your thoughts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007F#5PYeeeah, I think I'll pass.\x02\x03",

            "#1019FYou know, you didn't strike me as someone\x01",
            "who'd be into that sort of thing.\x02\x03",

            "Well, whatever. Here's a question for you:\x01",
            "was the whole 'poor archaeologist' thing a\x01",
            "total act, or what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1154FHaha. Putting the poverty aside, I actually\x01",
            "am an archaeologist.\x02\x03",

            "#1150FAnd as an aside, I picked up the pipe organ\x01",
            "during my time with the church.\x02\x03",

            "I may not be that Erebonian you spend so\x01",
            "much time with, but I daresay I'm decent,\x01",
            "wouldn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1004F#5PHang on, the church? Like the Septian...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#1151FI was something of an academic priest.\x02\x03",

            "#1154FA chance meeting with the Grandmaster\x01",
            "led to me discarding the path of faith.\x02\x03",

            "My knowledge of artifacts, paltry as it is, still\x01",
            "proves useful from time to time, thankfully.\x02\x03",

            "#1150FWith our current plan, in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1002F#5P...\x02\x03",

            "The one who tempted Colonel Richard\x01",
            "into starting the coup...\x02\x03",

            "And the one who arranged all the Gospel\x01",
            "experiments...\x02\x03",

            "It was you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1154FIt certainly was.\x02\x03",

            "#1151FAnd it was all for the sake of our cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1002F#5PYour 'Gospel Plan'?\x02\x03",

            "I saw something in the research\x01",
            "facility about that.\x02\x03",

            "Your plan is to take the Aureole,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1154F...'Take' the Aureole? That's not entirely\x01",
            "accurate...\x02\x03",

            "#1150F...but, for the purposes of this conversation,\x01",
            "it will suffice. Yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1005F#5PWhat IS the Aureole, anyway?\x01",
            "Why do you want it so bad?!\x02\x03",

            "I know it's said to be one of the treasures\x01",
            "of Aidios, but just what is it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1151FAh, for the moment, I must keep the exact\x01",
            "nature of the Aureole a secret.\x02\x03",

            "I would, after all, so hate to spoil the surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1019F#5PThe surprise. Right. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1150FOur plan has moved into its third phase.\x02\x03",

            "Very, very soon now, its true nature will\x01",
            "be plain to see.\x02\x03",

            "#1154FHaha... I can barely contain my anticipation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1002F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#1154FAnd once the Aureole has shown itself...\x02\x03",

            "#1151FThen... Then we will see the potential of\x01",
            "mankind unfurl before our eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F#5PThe 'potential of mankind'...\x02\x03",

            "Ragnard said something about that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#1153FOh? The holy beast was willing to bestow\x01",
            "his wisdom upon you?\x02\x03",

            "#1150FPerhaps you ARE doing more than simply\x01",
            "living in your father's shadow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1022F#5PSpare me the flattery.\x02\x03",

            "#1019FAnd what the hell? I keep asking you\x01",
            "things and you keep dodging the answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1154FDo forgive me. It wasn't my intention to be\x01",
            "so evasive.\x02\x03",

            "#1150FI can, however, easily answer the question\x01",
            "I know you want to ask most.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        "#1026F#5PThe...what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1151FWhat keeps you from asking it?\x02\x03",

            "Don't be afraid. Muster your courage\x01",
            "and ask it of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1003F#5P...\x02\x03",

            "Joshua... Where's Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#1154FHm... His exact location is currently\x01",
            "unknown to me.\x02\x03",

            "From what I've observed, he's up to\x01",
            "something with those sky bandits.\x02\x03",

            "Their movements have proven to be\x01",
            "quite elusive.\x02\x03",

            "#1150FThough he is alive and well, I can\x01",
            "assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1025F#5POkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#1154FJoshua's specialties are covert operation\x01",
            "and guerrilla warfare.\x02\x03",

            "I was the one who tuned him to excel at\x01",
            "such, but he has long since surpassed\x01",
            "even my greatest expectations.\x02\x03",

            "#1151FHeh... I gleefully await seeing the height\x01",
            "of his potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1002F#5PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#1153FCome now, you needn't look so angry.\x02\x03",

            "#1150FWhen Joshua was entrusted to my care,\x01",
            "his heart was akin to a glass ornament\x01",
            "dashed against a paving stone.\x02\x03",

            "He was my first attempt at rebuilding such\x01",
            "a shattered soul.\x02\x03",

            "#1154FIs it not natural, you think, for an academic\x01",
            "to be curious about the result of his work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1003F#5P...\x02\x03",

            "What did you tell Joshua on the day\x01",
            "of the queen's birthday celebrations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#1150FI merely removed the block on his memory\x01",
            "and told him the truth.\x02\x03",

            "#1154FThat he, once taken into your home, had\x01",
            "unwittingly been acting as a spy and sending\x01",
            "guild information to the society.\x02\x03",

            "That Richard's coup succeeded in its own right\x01",
            "because of him. And finally that, thanks to his\x01",
            "efforts, the ground was at last fertile for our plan.\x02\x03",

            "#1151FI even rewarded him! I formally released him\x01",
            "from his obligations to the society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1027F#5P...\x02\x03",

            "I finally get it...\x02\x03",

            "Why Joshua...that night...\x01",
            "Why he disappeared...\x02\x03",

            "Why he said goodbye with\x01",
            "that look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1150FMmm, yes, I must say I did find that\x01",
            "regrettable.\x02\x03",

            "To think Joshua would abandon you\x01",
            "so coldly after regaining himself!\x02\x03",

            "#1154FI recommended he just pretend he\x01",
            "knew nothing of it and continue his\x01",
            "life with you, but alas.\x02\x03",

            "#1151FI suppose my generosity backfired,\x01",
            "no?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    OP_6D(270, 420, 83800, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(386, 0)
    SetChrChipByIndex(0x101, 16)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #40
        0x101,
        (
            "#1025F#2PI'm amazed... I'm amazed you can even\x01",
            "say that.\x02\x03",

            "You were the one who chased Joshua\x01",
            "into a corner in the first place. He didn't\x01",
            "have a choice!\x02\x03",

            "#1027FSo he had to...to look like that...\x01",
            "and give his harmonica to me...\x02\x03",

            "And say...'Goodbye, Estelle'...\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1023F#3S#2PALL OF IT! EVERY LAST BIT!#2S\x02\x03",

            "#1023F#3S#2PIT'S ALL YOUR FAULT!!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1DDB():
        OP_6D(-660, 1500, 85500, 600)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1DDB)

    def lambda_1DF3():
        OP_6B(2200, 600)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1DF3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x101, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x9, 9)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, -990, 2500, 84790, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x1000)

    def lambda_1E48():
        OP_8F(0xFE, 0xFFFFFC22, 0x5DC, 0x14B36, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E48)

    def lambda_1E63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E63)
    OP_22(0x99, 0x0, 0x64)
    Sleep(300)
    OP_43(0x9, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x101, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_1ED6():
        OP_6D(-980, 1500, 81840, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ED6)

    def lambda_1EEE():
        OP_67(0, 3600, -10000, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1EEE)

    def lambda_1F06():
        OP_6B(2800, 300)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1F06)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x5)

    ChrTalk(    #42 op#5
        0x101,
        "#2PAgh!\x05\x02",
    )

    Sleep(500)
    WaitChrThread(0x101, 0x0)
    OP_99(0x101, 0x1, 0x3, 0x5DC)
    OP_22(0x20C, 0x0, 0x64)
    ClearChrFlags(0x9, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_99(0x9, 0x6, 0x7, 0x5DC)
    Sleep(500)

    ChrTalk(    #43
        0x9,
        "#121F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1021F#2PLoewe...\x02\x03",

            "The hell did you come from...?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(    #45
        0x9,
        (
            "#124F#6PI was here from the start.\x02\x03",

            "#120FYou simply didn't bother to notice.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #46
        "\x07\x05Tsk tsk! What an undignified performance.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_2070():
        OP_6D(-450, 1500, 84100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2070)

    def lambda_2088():
        OP_67(0, 3600, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2088)

    def lambda_20A0():
        OP_6B(2420, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20A0)

    def lambda_20B0():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20B0)
    SetChrPos(0xA, -5300, 1500, 85140, 135)
    SetChrPos(0xB, 5040, 1500, 85050, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    OP_43(0xA, 0x0, 0x0, 0x6)
    Sleep(500)
    OP_43(0xB, 0x0, 0x0, 0x7)
    Sleep(2000)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 570, 1500, 84590, 180)

    def lambda_212A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_212A)
    OP_22(0x99, 0x0, 0x64)
    OP_43(0x11, 0x1, 0x0, 0x8)
    OP_43(0x12, 0x1, 0x0, 0x9)
    Sleep(800)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0xC, 0x1)

    def lambda_2170():

        label("loc_2170")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2170")

    QueueWorkItem2(0x101, 3, lambda_2170)
    OP_99(0x101, 0x3, 0x0, 0x3E8)
    OP_44(0x101, 0x3)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C9")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared all of Bleublanc's Challenges\x01",              # 0
            "Set as cleared one or more of Bleublanc's Challenges\x01",      # 1
            "Set as ignored Bleublanc's Challenges\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_227B"),
        (1, "loc_2292"),
        (2, "loc_22A9"),
        (SWITCH_DEFAULT, "loc_22C0"),
    )


    label("loc_227B")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x4, 0x10)
    OP_28(0x78, 0x4, 0x10)
    OP_28(0xC4, 0x4, 0x10)
    Jump("loc_22C0")

    label("loc_2292")

    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_22C0")

    label("loc_22A9")

    OP_28(0x6C, 0x3, 0x10)
    OP_28(0x77, 0x3, 0x10)
    OP_28(0x78, 0x3, 0x10)
    OP_28(0xC4, 0x3, 0x10)
    Jump("loc_22C0")

    label("loc_22C0")

    FadeToBright(300, 0)

    label("loc_22C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22DD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22F1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2305")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2319")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_239C")

    ChrTalk(    #47
        0xA,
        (
            "#231F#3PYou performed so well in completing my\x01",
            "challenges, too.\x02\x03",

            "Did I not teach you to think before you act?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D6")

    label("loc_239C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2463")

    ChrTalk(    #48
        0xA,
        (
            "#232F#3PAnd to think this comes from someone\x01",
            "who rose to the occasion on some of my\x01",
            "challenges, too.\x02\x03",

            "I suppose it was not enough to teach you\x01",
            "to think before you act.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D6")

    label("loc_2463")


    ChrTalk(    #49
        0xA,
        (
            "#233F#3PHad you bothered to accept even one of\x01",
            "my challenges, you would have seen him.\x02\x03",

            "Think before you act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D6")


    ChrTalk(    #50
        0xB,
        (
            "#252F#4PC'mon, give her some credit.\x02\x03",

            "It takes balls to pick a fight with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "#244F#6PAgreed. Regardless of her skills,\x01",
            "her courage certainly is impressive.\x02\x03",

            "#240FThough I wonder if we should call\x01",
            "it courage or mere foolishness.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25CC():
        OP_6D(-450, 960, 82000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25CC)
    Sleep(500)
    OP_8F(0x101, 0xFFFFFBE6, 0x0, 0x12750, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #52
        0x101,
        "#1026F#2POh...crap...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 2800, 0, 79120, 225)
    SetMessageWindowPos(400, 150, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(    #53
        (
            "\x07\x05Haha. So you're the Divine Blade's\x01",
            "daughter?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_26A3():
        OP_6D(340, 480, 81240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_26A3)

    def lambda_26BB():
        OP_67(0, 4260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26BB)

    def lambda_26D3():
        OP_6B(2460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26D3)
    Sleep(500)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)
    LoadEffect(0x1, "map\\\\mp055_00.eff")
    SetChrFlags(0xD, 0x8000)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    PlayEffect(0x1, 0x1, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2752():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2752)
    OP_22(0x99, 0x0, 0x64)
    Sleep(1800)
    OP_82(0x1, 0x2)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #54
        0xD,
        "#853F#4PThis would be the first time we've met.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x0, 0x3, 0x5DC)

    ChrTalk(    #55
        0xD,
        (
            "#854F#4PI am Enforcer No. 0, Campanella the Fool.\x02\x03",

            "#851FNice to meet you. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xD, 0x3, 0x0, 0x5DC)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    Sleep(500)

    ChrTalk(    #56
        0x101,
        "#1020F#5PAnother one...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1010, 0, 67570, 0)

    NpcTalk(    #57
        0xE,
        "Girl's Voice",
        "#1PStop it, guys, you're scaring Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_28A7():
        OP_6D(-1070, 0, 74320, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28A7)

    def lambda_28BF():
        OP_6B(2600, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28BF)
    TurnDirection(0x101, 0xE, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_28E0():
        OP_6D(-890, 0, 78320, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28E0)

    def lambda_28F8():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28F8)
    OP_8E(0xE, 0xFFFFFBC8, 0x0, 0x1200C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #58
        0x101,
        "#1026F#5PRenne, too...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "#263F#2PYou don't need to worry, Estelle.\x02\x03",

            "#260FI know what I said last time, but we\x01",
            "aren't here to hurt you or anything.\x01",
            "Promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1004F#5PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_29D9():

        label("loc_29D9")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_29D9")

    QueueWorkItem2(0x101, 1, lambda_29D9)

    def lambda_29EA():
        OP_6D(-380, 950, 82220, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29EA)

    def lambda_2A02():
        OP_67(0, 4710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A02)

    def lambda_2A1A():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2A1A)

    def lambda_2A2A():
        OP_6E(360, 3000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2A2A)
    OP_8E(0xE, 0x172, 0x0, 0x126D8, 0x7D0, 0x0)
    OP_8E(0xE, 0x172, 0x0, 0x12FE8, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)

    ChrTalk(    #61
        0xE,
        (
            "#261F#2PHeeey, Professor!\x02\x03",

            "Why not ask Estelle right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#1154F#6PWell, now is as good a time as any.\x02",
    )

    CloseMessageWindow()

    def lambda_2ADC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2ADC)

    def lambda_2AEA():
        OP_6D(-940, 940, 81750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AEA)

    def lambda_2B02():
        OP_67(0, 4230, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B02)

    def lambda_2B1A():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B1A)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 14)

    def lambda_2B34():
        OP_8E(0xFE, 0xFFFFF5EC, 0x5DC, 0x14B4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B34)
    Sleep(200)

    def lambda_2B54():
        OP_8E(0xFE, 0xFFFFFB14, 0x5DC, 0x14438, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B54)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #63
        0x8,
        (
            "#1150F#6PHow about it, Estelle?\x02\x03",

            "Would you like to join Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1004F#2PUh... What?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #65
        0x101,
        (
            "#1016F#2PI'm sorry. I misheard that.\x02\x03",

            "#1008FWould you say that one more time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1154F#6PI asked if you would like to join the Society\x01",
            "of Ouroboros.\x02\x03",

            "#1151FYou wouldn't become a full-fledged\x01",
            "Enforcer right away, of course. You would\x01",
            "be more a candidate for the position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1020F#2PWh-Wh-Wh...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        "#1005F#2P#4SARE YOU INSANE?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1151F#6PCome now.\x02\x03",

            "It's hardly the leap of logic you're thinking.\x02\x03",

            "Joshua has been rather stubborn about\x01",
            "returning, but with you here, he would\x01",
            "undoubtedly come back to us--and to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1026F#2POh. Umm... Umm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #71
        0xE,
        (
            "#265F#5PEstelle, you wanna see Joshua again\x01",
            "more than anything else, right?\x02\x03",

            "If you join us, that'll come true right away!\x02\x03",

            "#261FWhat's there to even think about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #72
        0x101,
        (
            "#1003F#2PBut... But...\x02\x03",

            "I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#1150F#6PNow, Renne. Estelle might need some\x01",
            "time to weigh her options.\x02\x03",

            "#1154FWe will be departing the ship for a little\x01",
            "while on business, Estelle.\x02\x03",

            "You may give us your answer when we\x01",
            "return.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 19)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x8, 1)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xF, -1830, 0, 69620, 0)
    SetChrPos(0x10, -220, 0, 69620, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)

    def lambda_3073():
        OP_6D(360, 680, 80540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3073)

    def lambda_308B():
        OP_67(0, 3470, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_308B)

    def lambda_30A3():
        OP_6B(3220, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30A3)

    def lambda_30B3():
        OP_8E(0xFE, 0xFFFFF8DA, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_30B3)
    Sleep(100)

    def lambda_30D3():
        OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x12110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30D3)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #74
        0x8,
        (
            "#1151F#3PAnd I do apologize for this, but your\x01",
            "options must remain fairly limited during\x01",
            "your stay.\x02\x03",

            "Feel free to request anything you need,\x01",
            "but you'll be staying in your cabin.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x1C93)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5400   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2FC end

    def Function_3_31D6(): pass

    label("Function_3_31D6")

    OP_99(0x9, 0x9, 0xF, 0xDAC)
    SetChrChipByIndex(0x9, 3)
    OP_99(0x9, 0x0, 0x5, 0xDAC)
    OP_22(0x1F5, 0x0, 0x64)
    Return()

    # Function_3_31D6 end

    def Function_4_31F3(): pass

    label("Function_4_31F3")

    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)

    def lambda_3203():
        OP_8E(0xFE, 0xFFFFFC22, 0x5DC, 0x1465E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3203)
    Sleep(200)
    SetChrChipByIndex(0x101, 20)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x101, 0x4)

    def lambda_3232():
        OP_96(0xFE, 0xFFFFFC22, 0x708, 0x14690, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3232)
    Sleep(100)

    def lambda_3255():
        OP_99(0xFE, 0x0, 0x7, 0x8FC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3255)
    Sleep(100)
    OP_22(0x1F4, 0x0, 0x64)
    Return()

    # Function_4_31F3 end

    def Function_5_326A(): pass

    label("Function_5_326A")

    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x101, 11)

    def lambda_3289():
        OP_96(0xFE, 0xFFFFFC90, 0x0, 0x1374A, 0x5DC, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3289)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)

    def lambda_32B1():
        OP_96(0xFE, 0xFFFFFC68, 0x0, 0x12E3A, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32B1)
    WaitChrThread(0x101, 0x1)

    def lambda_32D4():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32D4)
    Sleep(100)

    def lambda_32F4():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32F4)
    Sleep(100)

    def lambda_3314():
        OP_8F(0xFE, 0xFFFFFCB8, 0x0, 0x12926, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3314)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_5_326A end

    def Function_6_3348(): pass

    label("Function_6_3348")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_335E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_335E)
    OP_8E(0xFE, 0xFFFFEEBC, 0x5DC, 0x14A78, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFFF01A, 0x5DC, 0x14780, 0x5DC, 0x0)
    Return()

    # Function_6_3348 end

    def Function_7_3393(): pass

    label("Function_7_3393")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_33A9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33A9)
    OP_8E(0xFE, 0xAAA, 0x5DC, 0x14B72, 0x5DC, 0x0)
    OP_8E(0xFE, 0x596, 0x5DC, 0x14438, 0x5DC, 0x0)
    OP_8C(0xFE, 205, 400)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_3393 end

    def Function_8_33EF(): pass

    label("Function_8_33EF")

    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 570, 1500, 84590, 180)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3416():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3416)
    ClearChrFlags(0x11, 0x80)
    OP_91(0x11, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x11, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_8_33EF end

    def Function_9_34B0(): pass

    label("Function_9_34B0")

    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 570, 1500, 84590, 180)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_34D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_34D7)
    ClearChrFlags(0x12, 0x80)
    OP_91(0x12, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0x12, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_9_34B0 end

    def Function_10_3571(): pass

    label("Function_10_3571")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(210, 0, 53260, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(551, 0)
    SetChrPos(0xD, -1190, 1500, 85710, 0)
    ClearChrFlags(0xD, 0x80)

    def lambda_35E0():
        OP_6D(-970, 5670, 90410, 8000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_35E0)

    def lambda_35F8():
        OP_67(0, 4170, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_35F8)

    def lambda_3610():
        OP_6B(3050, 8000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3610)

    def lambda_3620():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_3620)

    def lambda_3630():
        OP_6E(449, 8000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3630)
    OP_71(0x6, 0x4)
    OP_72(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-450, 1500, 86520, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    OP_71(0x4, 0x4)
    OP_79(0x9, 0x2)
    OP_7B()
    OP_0D()
    Sleep(500)

    ChrTalk(    #75
        0xD,
        (
            "#850F#4PHeehee. What fun that was!\x02\x03",

            "At the rate they're going, they'll be\x01",
            "in the Axis Pillar within the day.\x02\x03",

            "#855FAnd with things going this solidly\x01",
            "according to plan, there's almost no\x01",
            "point to me observing.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)
    Sleep(500)

    ChrTalk(    #76
        0xD,
        (
            "#853F#6PIt looks like I have a little time before\x01",
            "the curtains rise for the real final\x01",
            "act...\x02\x03",

            "#854FMaybe I can mess with Gilbert\x01",
            "a little until then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #77
        "\x07\x05And so Estelle and the Capuas escaped the Glorious.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #78
        "\x07\x05After several battles with pursuing jaegers...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        (
            "\x07\x05Estelle's team shook off pursuit and returned to the Cradle\x01",
            "District.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5801   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3571 end

    SaveToFile()

Try(main)
