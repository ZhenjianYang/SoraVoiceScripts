from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4202.x',
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
        'Queen Alicia',                         # 9
        '1st Lieutenant Schwarz',               # 10
        'Joshua',                               # 11
        'Olivier',                              # 12
        'Zin',                                  # 13
        '2nd Lieutenant Lorence',               # 14
        'Lorence Shadow',                       # 15
        'Lorence Shadow',                       # 16
        'Lorence Shadow',                       # 17
        'Lorence Shadow',                       # 18
        'Helmet',                               # 19
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH00010 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT07/CH00480 ._CH',             # 05
        'ED6_DT07/CH00482 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00120 ._CH',             # 09
        'ED6_DT07/CH00121 ._CH',             # 0A
        'ED6_DT07/CH00140 ._CH',             # 0B
        'ED6_DT07/CH00141 ._CH',             # 0C
        'ED6_DT07/CH02200 ._CH',             # 0D
        'ED6_DT07/CH00484 ._CH',             # 0E
        'ED6_DT07/CH00104 ._CH',             # 0F
        'ED6_DT07/CH00124 ._CH',             # 10
        'ED6_DT07/CH00144 ._CH',             # 11
        'ED6_DT06/CH20035 ._CH',             # 12
        'ED6_DT06/CH20036 ._CH',             # 13
        'ED6_DT06/CH20037 ._CH',             # 14
        'ED6_DT06/CH20044 ._CH',             # 15
        'ED6_DT07/CH00481 ._CH',             # 16
        'ED6_DT07/CH00011 ._CH',             # 17
        'ED6_DT07/CH00031 ._CH',             # 18
        'ED6_DT07/CH00071 ._CH',             # 19
        'ED6_DT06/CH20114 ._CH',             # 1A
        'ED6_DT06/CH20115 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH00480P._CP',             # 05
        'ED6_DT07/CH00482P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00120P._CP',             # 09
        'ED6_DT07/CH00121P._CP',             # 0A
        'ED6_DT07/CH00140P._CP',             # 0B
        'ED6_DT07/CH00141P._CP',             # 0C
        'ED6_DT07/CH02200P._CP',             # 0D
        'ED6_DT07/CH00484P._CP',             # 0E
        'ED6_DT07/CH00104P._CP',             # 0F
        'ED6_DT07/CH00124P._CP',             # 10
        'ED6_DT07/CH00144P._CP',             # 11
        'ED6_DT06/CH20035P._CP',             # 12
        'ED6_DT06/CH20036P._CP',             # 13
        'ED6_DT06/CH20037P._CP',             # 14
        'ED6_DT06/CH20044P._CP',             # 15
        'ED6_DT07/CH00481P._CP',             # 16
        'ED6_DT07/CH00011P._CP',             # 17
        'ED6_DT07/CH00031P._CP',             # 18
        'ED6_DT07/CH00071P._CP',             # 19
        'ED6_DT06/CH20114P._CP',             # 1A
        'ED6_DT06/CH20115P._CP',             # 1B
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x180,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x180,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x180,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x180,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2EA",          # 00, 0
        "Function_1_312",          # 01, 1
        "Function_2_35D",          # 02, 2
        "Function_3_33E4",         # 03, 3
        "Function_4_3412",         # 04, 4
        "Function_5_34B9",         # 05, 5
        "Function_6_3565",         # 06, 6
        "Function_7_35F5",         # 07, 7
    )


    def Function_0_2EA(): pass

    label("Function_0_2EA")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2F6"),
        (SWITCH_DEFAULT, "loc_311"),
    )


    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30E")
    OP_22(0x1C3, 0x1, 0x64)
    OP_A2(0x666)
    Event(0, 2)

    label("loc_30E")

    Jump("loc_311")

    label("loc_311")

    Return()

    # Function_0_2EA end

    def Function_1_312(): pass

    label("Function_1_312")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x39A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F")
    OP_22(0x1C3, 0x1, 0x64)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C")

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_347")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C")

    Return()

    # Function_1_312 end

    def Function_2_35D(): pass

    label("Function_2_35D")

    EventBegin(0x0)
    OP_28(0x4E, 0x1, 0x8)
    OP_6D(2050, 12000, 54240, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(54000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 2170, 12000, 62700, 0)
    SetChrPos(0xD, 4110, 12000, 65390, 180)
    SetChrPos(0x101, 1870, 12000, 45230, 0)
    SetChrPos(0x105, 1870, 12000, 45230, 0)
    SetChrPos(0x103, 1870, 12000, 45230, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x103, 9)
    SetChrChipByIndex(0x105, 11)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x800)
    FadeToBright(1000, 0)

    def lambda_445():
        OP_6D(1870, 12000, 56440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_445)

    def lambda_45D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_45D)

    def lambda_46F():
        OP_8E(0xFE, 0x730, 0x2EE0, 0xD566, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_46F)
    Sleep(500)

    def lambda_48F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48F)

    def lambda_4A1():
        OP_8E(0xFE, 0xBCC, 0x2EE0, 0xD0AC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A1)
    Sleep(500)

    def lambda_4C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4C1)

    def lambda_4D3():
        OP_8E(0xFE, 0x26C, 0x2EE0, 0xD19C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #0
        0x105,
        "#043FAre you all right, Grandmother?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#508FWe're here to rescue you,\x01",
            "Your Majesty!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #2
        0x8,
        "#093FKlaudia...and Estelle...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0xD,
        "Man's Voice",
        (
            "#4PSo, you're finally here... I was\x01",
            "getting quite bored with waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x51)

    def lambda_62A():
        OP_8E(0xD, 0xAD2, 0x2EE0, 0xF3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_62A)

    def lambda_645():

        label("loc_645")

        TurnDirection(0xD, 0x105, 0)
        OP_48()
        Jump("loc_645")

    QueueWorkItem2(0xD, 1, lambda_645)

    def lambda_656():
        OP_6D(2100, 13150, 60270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_656)

    def lambda_66E():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_66E)

    def lambda_67E():
        OP_6E(359, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_67E)

    def lambda_68E():
        OP_67(0, 6640, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_68E)

    def lambda_6A6():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6A6)
    Sleep(800)

    def lambda_6BB():
        OP_8F(0xFE, 0x88E, 0x2EE0, 0xF744, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6BB)
    Sleep(200)

    def lambda_6DB():
        OP_8E(0xFE, 0x83E, 0x2EE0, 0xDDC2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DB)
    Sleep(110)

    def lambda_6FB():
        OP_8E(0xFE, 0xD20, 0x2EE0, 0xDFB6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FB)
    Sleep(100)

    def lambda_71B():
        OP_8E(0xFE, 0x280, 0x2EE0, 0xE074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_71B)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #4
        0x101,
        (
            "#580FLieutenant Lorence!\x01",
            "What are you doing here...?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)

    ChrTalk(    #5
        0xD,
        (
            "#280F#6PHa ha... My duty is to guard\x01",
            "Her Majesty.\x02\x03",

            "Is it truly any wonder that\x01",
            "I'm here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#005FEnough of your crap!\x02\x03",

            "No matter how strong you are,\x01",
            "we've still got three-to-one\x01",
            "odds on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#023FThis one certainly seems skilled.\x02\x03",

            "Just who is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#005FCommander of the Intelligence\x01",
            "Division's Special Ops...\x01",
            "2nd Lieutenant Lorence Belgar!\x02\x03",

            "Former jaeger, and scout\x01",
            "for the colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "#280F#6PSo you've done your research,\x01",
            "I see. Most impressive.\x02\x03",

            "But what else would one expect of the\x01",
            "daughter of an S-ranked bracer...one\x01",
            "Cassius Bright, I believe...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#580F#3S!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#022FMy master's rank has never been\x01",
            "public knowledge, and yet...\x02\x03",

            "You are not one to be\x01",
            "trifled with, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "#280F#6PHa ha...\x01",
            "I know you, as well.\x02\x03",

            "Scherazard Harvey, also known as\x01",
            "the 'Silver Streak'. C-ranked.\x02\x03",

            "And very close to ascending\x01",
            "to B rank, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        "#022F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#043FP-Please...release my grandmother.\x02\x03",

            "If you were just fighting in the\x01",
            "employ of the colonel, there is\x01",
            "no further call to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xD,
        (
            "#280F#6PThere are more things in heaven\x01",
            "and earth than are dreamt of in\x01",
            "your philosophy...\x02\x03",

            "You see only the surface, like that\x01",
            "of a quartz grid...with no concept\x01",
            "of the forces at work within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        "#044FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        (
            "#281F#6PTake heed, Princess Klaudia.\x02\x03",

            "The nation is like an enormously\x01",
            "complex orbment.\x02\x03",

            "The people are like the units\x01",
            "of quartz that provide the power\x01",
            "and organize the system...\x02\x03",

            "And the territory which houses\x01",
            "them is the frame...\x02\x03",

            "If you lack the means to under-\x01",
            "stand how it works, then you are\x01",
            "unfit to be its queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#043F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#094FAn interesting metaphor...\x02\x03",

            "#090FYou may even be right.\x02\x03",

            "I certainly never expected to\x01",
            "hear a theory on the nature of\x01",
            "politics at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xD,
        (
            "#280F#6PHeh... Pardon my rudeness. You've no\x01",
            "need to hear my useless sermonizing,\x01",
            "Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#007FI...don't really understand\x01",
            "this all that well...\x02\x03",

            "#002F...but the general gist is\x01",
            "that you don't plan to let\x01",
            "the queen go, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        "#280F#6PAnd if I do not...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#005FObviously we'd take her back\x01",
            "by force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#024FIndeed... After we've come this far,\x01",
            "we certainly can't go back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        (
            "#049FYou don't give me the impression\x01",
            "that you bear us any ill will...\x02\x03",

            "#042F...but I WILL bring my blade to\x01",
            "bear on you, if it will get my\x01",
            "grandmother back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        (
            "#280F#6PHa ha... Good.\x02\x03",

            "In that case, let me show you a\x01",
            "little of what I can REALLY do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#004FHuh...?!\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 18)

    def lambda_10FA():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10FA)
    Sleep(500)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x40)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 3300, 12300, 62320, 0)
    OP_99(0xD, 0x1, 0x4, 0x514)
    ClearChrFlags(0x12, 0x80)

    def lambda_1147():
        OP_99(0xFE, 0x5, 0x7, 0x514)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1147)
    OP_8E(0x12, 0xDAC, 0x2EE0, 0xF30C, 0x1388, 0x0)
    OP_22(0xB1, 0x0, 0x64)

    def lambda_1170():
        OP_99(0xFE, 0x0, 0x7, 0x4B0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1170)
    OP_96(0x12, 0x1400, 0x2EE0, 0xF190, 0x2BC, 0x5DC)
    OP_96(0x12, 0x16D0, 0x2EE0, 0xF050, 0x190, 0x5DC)

    def lambda_11AE():
        OP_99(0xFE, 0x0, 0x7, 0x514)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_11AE)
    OP_8E(0x12, 0x1964, 0x2EE0, 0xEF74, 0x2BC, 0x0)
    Sleep(500)

    ChrTalk(    #28
        0xD,
        "#284F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#580FSilver hair...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        (
            "#022FNo... \x01",
            "It's ash blond...\x02\x03",

            "I'd guess that you were born\x01",
            "somewhere up north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        (
            "#285F#6PHa ha...\x01",
            "Indeed, you are correct.\x02\x03",

            "Though it's closer than\x01",
            "you might think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#043FWha...?\x02",
    )

    CloseMessageWindow()
    OP_1D(0x2B)

    def lambda_12C5():
        OP_6B(2000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12C5)
    Sleep(500)
    Fade(500)
    ClearChrFlags(0xD, 0x2)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0xD,
        (
            "#286F#6PI trust you will not be offended\x01",
            "if I choose not to go easy on you,\x01",
            "simply because you are women.\x02\x03",

            "#283FShall we, then?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 22)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1394():
        OP_92(0xFE, 0x105, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1394)

    def lambda_13A9():
        OP_6D(2100, 13150, 57270, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_13A9)
    Sleep(400)
    OP_44(0xD, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x105, 0xFF)
    SetChrFlags(0xD, 0x20)
    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrPos(0x101, 3360, 12000, 57270, 0)
    SetChrPos(0x105, 2110, 12000, 56770, 0)
    SetChrPos(0x103, 640, 12000, 57460, 0)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 5)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_142D"),
        (SWITCH_DEFAULT, "loc_18C1"),
    )


    label("loc_142D")

    OP_83(0x16, 0x0)
    LoadEffect(0x0, "monster\\\\msc0280.eff")
    OP_28(0x4E, 0x1, 0x10)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 14)
    SetChrPos(0xD, 2220, 12000, 61180, 180)
    OP_2B(0x4D, 0x3)
    OP_6B(2300, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #34
        0xD,
        (
            "#286F#6PAmazing... I hadn't realized\x01",
            "that you were this strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#582F*huff* *huff*\x02\x03",

            "#005FYou were holding back in the\x01",
            "finals, weren't you?!\x02\x03",

            "We should never have even\x01",
            "stood a chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#2P#522FI-I'm impressed we beat\x01",
            "this monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        "#049FI... I can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "#284F#6PEstelle Bright... I apologize for\x01",
            "treating you as an unworthy opponent.\x02\x03",

            "Perhaps one day you may\x01",
            "reach your father's level...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#004FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        "#285F#6PHowever...that day has yet to arrive.\x02",
    )

    CloseMessageWindow()

    def lambda_1677():
        OP_6D(2400, 12000, 57540, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1677)
    OP_99(0xD, 0x3, 0x0, 0x7D0)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrPos(0xE, 2220, 12000, 61180, 180)
    SetChrPos(0xF, 2220, 12000, 61180, 180)
    SetChrPos(0x10, 2220, 12000, 61180, 180)
    SetChrPos(0x11, 2220, 12000, 61180, 180)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(90)
    OP_43(0xE, 0x1, 0x0, 0x4)
    Sleep(90)
    OP_43(0xF, 0x1, 0x0, 0x4)
    Sleep(90)
    OP_43(0x10, 0x1, 0x0, 0x4)
    Sleep(90)
    OP_43(0x11, 0x1, 0x0, 0x4)
    OP_A6(0x0)

    def lambda_1752():
        OP_67(0, 7820, -10000, 700)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1752)

    def lambda_176A():
        OP_6C(24000, 700)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_176A)
    OP_A6(0x1)
    Sleep(130)
    PlayEffect(0x0, 0xFF, 0xFF, 2360, 12050, 57260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0x2)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 17)
    TurnDirection(0x105, 0xD, 0)

    def lambda_17D1():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_17D1)

    def lambda_17E7():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17E7)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 16)
    TurnDirection(0x103, 0xD, 0)

    def lambda_180E():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_180E)

    def lambda_1824():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1824)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 15)
    TurnDirection(0x101, 0xD, 0)

    def lambda_184B():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_184B)

    def lambda_1861():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1861)
    Sleep(500)

    ChrTalk(    #41 op#A op#5
        0x101,
        "#504F#2P#8AAaaaahhh?!\x05\x02",
    )


    ChrTalk(    #42 op#A op#5
        0x103,
        "#523F#8AAck...!\x05\x02",
    )


    ChrTalk(    #43 op#A op#5
        0x105,
        "#4P#541F#8AAgh...!!\x05\x02",
    )

    Sleep(2500)
    Jump("loc_1AA5")

    label("loc_18C1")

    OP_28(0x4E, 0x1, 0x20)
    OP_6C(24000, 0)
    OP_67(0, 7820, -10000, 0)
    OP_6D(2400, 12000, 57540, 0)
    OP_6B(2300, 0)
    SetChrChipByIndex(0x105, 17)
    SetChrChipByIndex(0x103, 16)
    SetChrChipByIndex(0x101, 15)
    SetChrSubChip(0x105, 2)
    SetChrSubChip(0x103, 2)
    SetChrSubChip(0x101, 2)
    SetChrPos(0xD, 1970, 12000, 58030, 182)
    SetChrPos(0x105, 1500, 12000, 55600, 359)
    SetChrPos(0x103, -500, 12000, 57130, 49)
    SetChrPos(0x101, 4000, 12000, 56700, 290)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #44
        0xD,
        (
            "#284F#6P...How disappointing.\x02\x03",

            "I had thought you would prove\x01",
            "more of a challenge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#581F#4PH-How...\x02\x03",

            "How can he be so much stronger\x01",
            "than during the tournament...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#522FHe was probably holding\x01",
            "back deliberately...\x02\x03",

            "He might be as strong as\x01",
            "Master Cassius...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x105,
        (
            "#049FGrandmother...\x01",
            "I...I'm sorry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA5")

    label("loc_1AA5")


    ChrTalk(    #48
        0x8,
        "#095F#6PKlaudia! Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_1ACA():
        OP_8E(0xFE, 0x6F4, 0x2EE0, 0xF1EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ACA)
    Sleep(200)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)

    def lambda_1AFE():
        OP_6D(2150, 12000, 59650, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AFE)
    OP_8C(0xD, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #49
        0xD,
        (
            "#284F#2PThat will be far enough, Your\x01",
            "Majesty, if you please.\x02\x03",

            "They are not mortally wounded,\x01",
            "I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#093F#6P...\x02\x03",

            "Your eyes betray much...\x02\x03",

            "You are so young...yet you have\x01",
            "endured such hardships already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        (
            "#283F#2P...\x02\x03",

            "#286FYour Majesty, you are hardly\x01",
            "qualified to feel pity for me.\x02\x03",

            "You, who know the name of 'Hamel'...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x8,
        "#097F#6P#3S...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    def lambda_1CB3():

        label("loc_1CB3")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_1CB3")

    QueueWorkItem2(0xD, 1, lambda_1CB3)

    def lambda_1CC4():
        OP_6D(2150, 12000, 61000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CC4)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xD, 0xB0E, 0x2EE0, 0xF1FE, 0x1F4, 0x1388)
    TurnDirection(0x8, 0xD, 400)
    TurnDirection(0x105, 0xD, 0)

    def lambda_1D06():
        OP_99(0x105, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D06)
    Sleep(100)
    TurnDirection(0x101, 0xD, 0)

    def lambda_1D22():
        OP_99(0x101, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D22)
    Sleep(100)
    TurnDirection(0x103, 0xD, 0)

    def lambda_1D3E():
        OP_99(0x103, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D3E)
    WaitChrThread(0x105, 0x1)
    SetChrChipByIndex(0x105, 11)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 7)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 9)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #53
        0xD,
        (
            "#285FIt's almost time.\x02\x03",

            "I will return Her Majesty to\x01",
            "you, just as you wished.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)

    ChrTalk(    #54
        0x101,
        "#580FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "#286FIf you wish to stop the colonel,\x01",
            "you had best hurry below.\x02\x03",

            "You may well already be too late...\x02\x03",

            "But you may be able to prevent any further\x01",
            "needless damage from occurring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#092F#3PBelow...?\x02\x03",

            "You cannot mean beneath there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "#285FHeh... However unpleasant you may\x01",
            "find it, I was certain that you would \x01",
            "understand the significance.\x02\x03",

            "You can show them the way.\x02\x03",

            "#286FAnd now, I bid you adieu.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\evsepith.eff")

    def lambda_1F8B():

        label("loc_1F8B")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1F8B")

    QueueWorkItem2(0x8, 1, lambda_1F8B)
    ClearChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x4)

    def lambda_1FA6():
        OP_6D(1740, 12000, 71200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FA6)

    def lambda_1FBE():
        OP_6E(359, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FBE)

    def lambda_1FCE():
        OP_67(0, 6450, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1FCE)

    def lambda_1FE6():
        OP_6C(90000, 2500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1FE6)
    OP_20(0x5DC)
    SetChrFlags(0xD, 0x20)
    OP_8C(0xD, 0, 600)
    ClearChrFlags(0xD, 0x20)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x78, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x50, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x3C, 0x0)
    SetChrPos(0xE, 2830, 12000, 61950, 0)
    SetChrPos(0xF, 2830, 12000, 61950, 0)
    SetChrPos(0x10, 2830, 12000, 61950, 0)
    SetChrPos(0x11, 2830, 12000, 61950, 0)
    OP_43(0xD, 0x0, 0x0, 0x7)
    Sleep(150)
    OP_43(0xE, 0x0, 0x0, 0x6)
    Sleep(150)
    OP_43(0xF, 0x0, 0x0, 0x6)
    Sleep(150)
    OP_43(0x10, 0x0, 0x0, 0x6)
    Sleep(150)
    OP_43(0x11, 0x0, 0x0, 0x6)

    def lambda_20B3():
        OP_6C(110000, 2500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_20B3)
    Sleep(1100)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    SetChrPos(0x101, 4270, 12000, 59160, 0)
    SetChrPos(0x105, 1920, 12000, 58210, 0)
    SetChrPos(0x103, 10, 12000, 59190, 0)
    Sleep(3000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_211D():
        OP_6D(2090, 12000, 65720, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_211D)

    def lambda_2135():
        OP_6B(2840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2135)

    def lambda_2145():
        OP_6C(129000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2145)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #58
        0x101,
        "#005F#3PHey!!\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)

    def lambda_217D():
        OP_8E(0xFE, 0xEEC, 0x2EE0, 0x1064E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_217D)

    ChrTalk(    #59
        0x103,
        "#024F#3PIs he insane?!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)

    def lambda_21C9():
        OP_8E(0xFE, 0x2EE, 0x2EE0, 0x106DA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21C9)
    Sleep(500)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)

    def lambda_21F9():
        OP_8E(0xFE, 0x6EA, 0x2EE0, 0xED4E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21F9)
    WaitChrThread(0x105, 0x1)

    def lambda_2219():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2219)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #60
        0x101,
        (
            "#580FH-He's gone...\x02\x03",

            "Did he drop into the lake?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #61
        0x103,
        (
            "#022FBut the water's undisturbed...\x02\x03",

            "Just who is this guy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        "#043FGrandmother! Are you hurt?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#090F#6PI am unharmed, Klaudia.\x01",
            "He never laid a hand on me.\x02\x03",

            "#094FBut more importantly...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xB, 1870, 12000, 45230, 0)
    SetChrPos(0xA, 1870, 12000, 45230, 0)
    SetChrPos(0xC, 1870, 12000, 45230, 0)
    SetChrPos(0x9, 1870, 12000, 45230, 0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #64
        0xA,
        "Boy's Voice",
        "#3PEstelle!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x11)

    def lambda_23E5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23E5)

    def lambda_23F3():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23F3)

    def lambda_2401():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2401)

    def lambda_240F():
        OP_6D(2540, 12000, 61390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_240F)

    def lambda_2427():
        OP_67(0, 9350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2427)

    def lambda_243F():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_243F)
    OP_43(0xD, 0x1, 0x0, 0x3)
    SetChrChipByIndex(0xA, 23)

    def lambda_245B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_245B)

    def lambda_246D():
        OP_8E(0xFE, 0xD2A, 0x2EE0, 0xE394, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_246D)
    Sleep(500)
    SetChrChipByIndex(0x9, 26)

    def lambda_2492():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2492)

    def lambda_24A4():
        OP_8E(0xFE, 0x7D0, 0x2EE0, 0xE876, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24A4)
    Sleep(500)
    SetChrChipByIndex(0xB, 24)

    def lambda_24C9():

        label("loc_24C9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_24C9")

    QueueWorkItem2(0xB, 1, lambda_24C9)

    def lambda_24DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_24DA)

    def lambda_24EC():
        OP_8E(0xFE, 0x816, 0x2EE0, 0xE204, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_24EC)
    Sleep(500)
    SetChrChipByIndex(0xC, 25)

    def lambda_2511():

        label("loc_2511")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2511")

    QueueWorkItem2(0xC, 1, lambda_2511)

    def lambda_2522():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2522)

    def lambda_2534():
        OP_8E(0xFE, 0x2C6, 0x2EE0, 0xE448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2534)

    def lambda_254F():
        OP_8E(0xFE, 0xDF2, 0x2EE0, 0xE826, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_254F)
    Sleep(500)

    def lambda_256F():
        OP_8E(0xFE, 0x96, 0x2EE0, 0xEBB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_256F)

    def lambda_258A():
        OP_6D(2140, 12000, 59300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_258A)

    def lambda_25A2():
        OP_6E(307, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25A2)
    SetChrFlags(0x105, 0x40)
    OP_8E(0x105, 0xB22, 0x2EE0, 0xF000, 0x7D0, 0x0)
    TurnDirection(0x105, 0x9, 400)
    WaitChrThread(0x103, 0x1)

    def lambda_25D7():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_25D7)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #65
        0x101,
        (
            "#004FJoshua?!\x02\x03",

            "#001FThank Aidios you're all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#010F#4PYou, too...\x02\x03",

            "Since Colonel Richard and Lieu-\x01",
            "tenant Lorence weren't in the\x01",
            "castle, I started to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#505FThe red helmet guy was here\x01",
            "just a minute ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#014F#4PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#522FHe jumped over that handrail\x01",
            "and, well, who knows...\x02\x03",

            "#025FHe's some kind of monster,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "#013F#4PI... I see...\x02\x03",

            "#015FPraise Aidios for keeping you safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#008FJoshua...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 1)
    OP_8E(0x9, 0x730, 0x2EE0, 0xEBD2, 0x7D0, 0x0)

    ChrTalk(    #72
        0x9,
        (
            "#171F#2PYour Majesty... It's good to\x01",
            "see you unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#091FWell met, Lieutenant Schwarz.\x02\x03",

            "#090FIndeed, I owe all of you a\x01",
            "debt of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_285C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_285C)

    def lambda_286A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_286A)

    def lambda_2878():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2878)

    def lambda_2886():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2886)

    def lambda_2894():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2894)

    def lambda_28A2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_28A2)

    ChrTalk(    #74
        0xB,
        "#031F#4PYou are far too kind, Your Majesty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xC,
        (
            "#070F#4PWe're just glad to be of help.\x02\x03",

            "#074FI don't think this is over\x01",
            "yet, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "#175F#2PWe've dealt with the Special Ops\x01",
            "inside the castle, but I'm afraid\x01",
            "there are bad tidings...\x02\x03",

            "Army reinforcements from every\x01",
            "province are on their way to\x01",
            "Grancel.\x02\x03",

            "From the sounds of it, the\x01",
            "Intelligence Division is\x01",
            "somehow maintaining control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#093FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#178F#2PTime is short, my Liege.\x02\x03",

            "I must ask that you board the\x01",
            "I.D. ship and escape at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#094FNo... That I cannot do.\x02\x03",

            "#092FThe situation has grown more dire.\x02\x03",

            "Colonel Richard must be stopped,\x01",
            "whatever the cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#173F#2PWh-What do you mean,\x01",
            "Your Majesty?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x3E8)
    Fade(1000)
    OP_6D(2200, 12000, 60780, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 3190, 12000, 60950, 270)
    OP_21()
    OP_0D()
    OP_1D(0x21)
    Sleep(500)

    ChrTalk(    #81
        0x8,
        (
            "#093FLast night, I finally understood\x01",
            "the true intentions of which the\x01",
            "colonel spoke.\x02\x03",

            "He wants the Shining Ring...\x01",
            "the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#004FAureole...\x02\x03",

            "Why does that sound so familiar...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#015F#4PIt's one of the Sept-Terrions\x01",
            "that Aidios gave the ancients...\x02\x03",

            "#012FThe legend says that it has the\x01",
            "power to control nature itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#505FOh, yeah.\x01",
            "Professor Alba told us about it.\x02\x03",

            "But I thought that was just some\x01",
            "silly story that was passed down\x01",
            "through the church...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "#094F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#580FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xB,
        (
            "#032FHrm...\x01",
            "So it does exist?\x02\x03",

            "And it lies somewhere within Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#093FAccording to an old legend\x01",
            "of the royal family...\x02\x03",

            "#094F'The Shining Ring shall bring catastrophe,\x01",
            "condemning the souls of men to eternal\x01",
            "purgatory.'\x02\x03",

            "'It has been sealed within the interval of the\x01",
            "blackest dark, that we might retain our\x01",
            "humanity.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xC,
        (
            "#074F'Condemning the souls of men to\x01",
            "eternal purgatory'...?\x02\x03",

            "#072FWell, that's not a little ominous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#092FThese words have been passed down\x01",
            "in the royal family as a warning.\x02\x03",

            "Perhaps this 'Shining Ring' truly\x01",
            "was so dangerous that the royal\x01",
            "family's ancestors sealed it away.\x02\x03",

            "Also, there was that massive\x01",
            "orbal reaction that was detected\x01",
            "beneath the city...\x02\x03",

            "If one takes both of these\x01",
            "into account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "#012F#4PThis Shining Ring must be sealed\x01",
            "away underneath Grancel.\x02\x03",

            "It makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#093FYes...and I believe that the colonel\x01",
            "has reached the same conclusion.\x02\x03",

            "There remain no details of what,\x01",
            "exactly, the Shining Ring is...\x02\x03",

            "...but I believe there will be\x01",
            "grave danger for all, should it\x01",
            "be restored.\x02\x03",

            "It could be a disaster on par with\x01",
            "the Great Collapse of legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        "#043FN-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#522FIncredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#002FE-Excuse me, Your Majesty!\x02\x03",

            "Lieutenant Lorence told us\x01",
            "to go underground...\x02\x03",

            "...but what did that really mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#094FThere is a mysterious room\x01",
            "within Grancel Castle...\x02\x03",

            "...where nothing, not even a grain of\x01",
            "rice, has been kept in generations. \x01",
            "Forbidden since long ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x105,
        "#044FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        "#172FYou mean the Treasury?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_28(0x4E, 0x1, 0x40)
    OP_28(0x4E, 0x1, 0x80)
    OP_28(0x4E, 0x1, 0x100)
    OP_28(0x4E, 0x1, 0x200)
    OP_28(0x4E, 0x1, 0x400)
    OP_28(0x4F, 0x4, 0x2)
    OP_28(0x4F, 0x4, 0x4)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_35D end

    def Function_3_33E4(): pass

    label("Function_3_33E4")

    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 2)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x9, 27)
    WaitChrThread(0xB, 0x3)
    SetChrChipByIndex(0xB, 3)
    WaitChrThread(0xC, 0x3)
    SetChrChipByIndex(0xC, 4)
    Return()

    # Function_3_33E4 end

    def Function_4_3412(): pass

    label("Function_4_3412")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_96(0xFE, 0x83E, 0x2EE0, 0xEB28, 0x190, 0x1770)
    SetChrChipByIndex(0xFE, 6)

    def lambda_3448():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3448)
    OP_96(0xFE, 0x79E, 0x3A98, 0xE6AA, 0xBB8, 0x1F40)
    OP_A2(0x0)
    ClearChrFlags(0xFE, 0x400)
    Sleep(500)
    OP_A2(0x1)

    def lambda_347F():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_347F)
    OP_96(0xFE, 0x744, 0x2EE0, 0xE204, 0x0, 0x3A98)
    OP_A2(0x2)
    Sleep(2000)

    def lambda_34AE():
        OP_99(0xFE, 0x3, 0xB, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34AE)
    Return()

    # Function_4_3412 end

    def Function_5_34B9(): pass

    label("Function_5_34B9")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_96(0xFE, 0x83E, 0x2EE0, 0xEB28, 0x190, 0x1770)
    SetChrChipByIndex(0xFE, 6)

    def lambda_34EF():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_34EF)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0x79E, 0x3A98, 0xE6AA, 0xBB8, 0x1F40)
    OP_A2(0x0)
    ClearChrFlags(0xFE, 0x400)
    Sleep(500)
    OP_A2(0x1)

    def lambda_352B():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_352B)
    OP_96(0xFE, 0x744, 0x2EE0, 0xE204, 0x0, 0x3A98)
    OP_A2(0x2)
    Sleep(2000)

    def lambda_355A():
        OP_99(0xFE, 0x3, 0xB, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_355A)
    Return()

    # Function_5_34B9 end

    def Function_6_3565(): pass

    label("Function_6_3565")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0x992, 0x2EE0, 0xF622, 0x1770, 0x0)
    OP_8E(0xFE, 0x762, 0x2EE0, 0xFE60, 0x1770, 0x0)
    OP_96(0xFE, 0x7F8, 0x3066, 0x10888, 0x320, 0xDAC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 20)
    ClearChrFlags(0xFE, 0x80)

    def lambda_35D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35D1)
    OP_96(0xFE, 0x73A, 0x1194, 0x132A4, 0x3E8, 0xFA0)
    Return()

    # Function_6_3565 end

    def Function_7_35F5(): pass

    label("Function_7_35F5")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0x992, 0x2EE0, 0xF622, 0x1770, 0x0)
    OP_8E(0xFE, 0x762, 0x2EE0, 0xFE60, 0x1770, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xFE, 0x7F8, 0x3066, 0x10888, 0x320, 0xDAC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 20)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3666():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3666)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    OP_96(0xFE, 0x73A, 0x1194, 0x132A4, 0x3E8, 0xFA0)
    Return()

    # Function_7_35F5 end

    SaveToFile()

Try(main)
