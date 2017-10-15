from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0000   ._SN',
        MapName             = 'event',
        Location            = 'E0000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Santos',                               # 9
        'Passenger',                            # 10
        'Young Passenger',                      # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 4000,
        Unknown_08              = -4500,
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
        'ED6_DT07/CH01660 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01660P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
    )

    DeclNpc(
        X                   = -3050,
        Z                   = 5000,
        Y                   = 8470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -1600,
        Z                   = 5000,
        Y                   = -4820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3510,
        Z                   = 5000,
        Y                   = -4010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_134",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_2BC",          # 03, 3
        "Function_4_549",          # 04, 4
        "Function_5_610",          # 05, 5
        "Function_6_6BA",          # 06, 6
        "Function_7_1FCE",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_133")

    Return()

    # Function_0_122 end

    def Function_1_134(): pass

    label("Function_1_134")

    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)
    Return()

    # Function_1_134 end

    def Function_2_13F(): pass

    label("Function_2_13F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2A6")

    label("loc_164")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2A6")

    label("loc_17D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2A6")

    label("loc_196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2A6")

    label("loc_1AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2A6")

    label("loc_1C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2A6")

    label("loc_1E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2A6")

    label("loc_1FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2A6")

    label("loc_213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2A6")

    label("loc_22C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2A6")

    label("loc_245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2A6")

    label("loc_25E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_277")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2A6")

    label("loc_277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2A6")

    label("loc_290")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2A6")

    label("loc_2BB")

    Return()

    # Function_2_13F end

    def Function_3_2BC(): pass

    label("Function_3_2BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 3)), scpexpr(EXPR_END)), "loc_3BB")

    ChrTalk(    #0
        0xFE,
        (
            "I'm now off to inspect the Sapphirl Tower\x01",
            "in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "After Her Majesty's birthday celebrations,\x01",
            "there were sightings of odd phenomena\x01",
            "around the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "A little late, but better to investigate now\x01",
            "than never, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_545")

    label("loc_3BB")

    OP_A2(0x120B)

    ChrTalk(    #3
        0xFE,
        "*sigh* Such a pity...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Thanks to the clouds, you can't even\x01",
            "see the Sapphirl Tower from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'm a researcher with the History Museum.\x01",
            "You know the towers, right? I'm here to\x01",
            "inspect those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "After Her Majesty's birthday celebrations,\x01",
            "there were sightings of odd phenomena\x01",
            "around the Tetracyclic Towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "A little late, but better to investigate now\x01",
            "than never, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545")

    TalkEnd(0xFE)
    Return()

    # Function_3_2BC end

    def Function_4_549(): pass

    label("Function_4_549")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5B2")

    ChrTalk(    #8
        0xFE,
        "Haha, kids are always so fearless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "My knees are shaking just from\x01",
            "being out here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C")

    label("loc_5B2")

    OP_A2(0x0)

    ChrTalk(    #10
        0xFE,
        (
            "H-Hey! Don't get too close\x01",
            "to the edge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "What'll happen if you fall, eh?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_60C")

    TalkEnd(0xFE)
    Return()

    # Function_4_549 end

    def Function_5_610(): pass

    label("Function_5_610")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_668")

    ChrTalk(    #12
        0xFE,
        "Heeey, Papa, c'mere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The mountains and rivers\x01",
            "all look so small!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6")

    label("loc_668")

    OP_A2(0x1)

    ChrTalk(    #14
        0xFE,
        "Wooow, this is so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Heeey, look, look!\x01",
            "That tree is so tiny!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B6")

    TalkEnd(0xFE)
    Return()

    # Function_5_610 end

    def Function_6_6BA(): pass

    label("Function_6_6BA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CD")
    Call(0, 7)

    label("loc_6CD")

    StopSound(0x1ADB0, 0x249F0, 0x0)
    OP_6D(600, 5000, 44810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(7230, 0)
    OP_6C(143000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 3260, 5000, -4580, 85)
    SetChrPos(0xF7, 3270, 5000, -3730, 101)
    StopSound(0x9C40, 0x1ADB0, 0x32C8)
    OP_C8(0x80, 0x46, "C_PLAC29._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_76A():
        OP_6D(4040, 5000, -3270, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A)

    def lambda_782():
        OP_67(0, 10000, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_782)

    def lambda_79A():
        OP_6B(3500, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79A)
    Sleep(4000)

    def lambda_7AF():
        OP_6C(53000, 7000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7AF)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(4040, 5000, -3270, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(53000, 0)
    OP_6E(332, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_130D")

    ChrTalk(    #16
        0x101,
        (
            "#1011FAhhhh! What a nice day...\x02\x03",

            "The tourists gotta be flooding the streets\x01",
            "in Ruan if the weather's like this there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#1P#051FMaybe.\x02\x03",

            "They got bigger things heatin' the\x01",
            "place up than tourism, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #18
        0x101,
        (
            "#1004FOther than tourism?\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #19
        0x106,
        (
            "#1P#053FThe election for the new mayor.\x02\x03",

            "Apparently, there's two popular candidates\x01",
            "to replace old Dalmore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1011FSo it's, like, an actual fight\x01",
            "of an election? Neat.\x02\x03",

            "#1015FAnd, thinking about it,\x01",
            "I guess it is about time, huh?\x02\x03",

            "They can't just let the\x01",
            "mayor's office sit empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#1P#051FYeah, whole thing's been a bit\x01",
            "of a mess ever since you guys\x01",
            "blew that case wide open.\x02\x03",

            "I heard about what you guys did from Jean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016FAh, haha...\x02\x03",

            "#1008FYeah, after you left, me, Joshua\x01",
            "and Kloe worked on that.\x02\x03",

            "Well, we had some help from a reporter\x01",
            "too, and the actual arrest was done by\x01",
            "Lt. Schwarz of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#1P#051FHeh, even better! You're smart enough\x01",
            "to see it wasn't all just you.\x02\x03",

            "#551FBy 'Kloe,' though, you mean the girl in the\x01",
            "uniform, right? A.K.A....Princess Klaudia?\x02\x03",

            "Man, that blew my friggin' mind\x01",
            "when I heard that in the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1016FHaha, yeah, I know what you mean.\x02\x03",

            "#1015FY'know, I haven't seen Kloe since\x01",
            "the birthday festival...or Olivier,\x01",
            "I guess. For better or worse.\x02\x03",

            "#1003FAnd not just them... Tita, too...and Zin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#1P#552FI told Tita and her old fogey\x01",
            "about what was up with you.\x02\x03",

            "I figured they'd worry too much\x01",
            "if they were kept in the dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1025FOh... Thanks, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x106,
        (
            "#1P#053FYeah, well, you'd better send 'em\x01",
            "a letter soon, or meet 'em in person,\x01",
            "or whatever. They miss you.\x02\x03",

            "#050FOh, and Zin went back to\x01",
            "Calvard after the festival.\x02\x03",

            "He said to give you his best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1025FI see...\x01",
            "I wish I could've said goodbye...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x106,
        (
            "#1P#051FAs for the princess, pretty sure\x01",
            "she went back to the Jenis Royal Academy.\x02\x03",

            "We'll be in Ruan for a while, so\x01",
            "I think we can find some time\x01",
            "to drop in and say hi, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1016FYeah... You're right.\x02\x03",

            "#1008FHeheh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        "#1P#055FWhat? Did I say something funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1012FOh, no, not really.\x02\x03",

            "#1017FI was just thinking... You're a lot more\x01",
            "thoughtful than you look, Agate.\x02\x03",

            "You even offered to let me do some\x01",
            "shopping before we left the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #33
        0x106,
        (
            "#1P#552FThoughtful?! I'm not... I mean,\x01",
            "I am, but... Aww, forget it!\x02\x03",

            "#050FWhatever. I'm gonna go take\x01",
            "a nap in my seat till we arrive.\x02\x03",

            "Don't get so absorbed in wandering\x01",
            "around that you forget to get off\x01",
            "at Ruan!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 315, 400)

    def lambda_11CC():
        OP_6D(1540, 5000, -2430, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_11CC)

    def lambda_11E4():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_11E4)
    OP_8E(0x106, 0xFFFFFFE2, 0x13EC, 0xFFFFF9A2, 0x7D0, 0x0)
    OP_8C(0x106, 14, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x0)

    def lambda_122F():

        label("loc_122F")

        TurnDirection(0x101, 0x106, 0)
        OP_48()
        Jump("loc_122F")

    QueueWorkItem2(0x101, 0, lambda_122F)
    OP_8E(0x106, 0xFFFFFFE2, 0x13EC, 0x10E, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x800)

    ChrTalk(    #34
        0x101,
        (
            "#1016FAgate, you really do try too hard sometimes...\x02\x03",

            "#1006FAnyway, think I'll take his advice!\x01",
            "Time for a bit of looking around\x01",
            "before we arrive...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    RemoveParty(0x5, 0xFF)
    Jump("loc_1FC3")

    label("loc_130D")


    ChrTalk(    #35
        0x101,
        (
            "#1011FAhhhh! What a nice day...\x02\x03",

            "The tourists gotta be flooding the streets\x01",
            "in Ruan if the weather's like this there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#1P#021FNo doubt!\x02\x03",

            "#020FUnfortunately, Ruan's pretty busy getting\x01",
            "'excited' over something other than tourism.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #37
        0x101,
        "#1004FOther than tourism? What do you mean?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #38
        0x103,
        (
            "#1P#020FThe mayoral elections.\x02\x03",

            "They're only now gearing up to hold\x01",
            "the special election for a new mayor\x01",
            "after the last one was arrested.\x02\x03",

            "I understand there are two\x01",
            "major candidates slugging\x01",
            "it out for the seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1011FSo it's, like, an actual fight\x01",
            "of an election? Neat.\x02\x03",

            "#1015FAnd, thinking about it,\x01",
            "I guess it is about time, huh?\x02\x03",

            "They can't just let the mayor's\x01",
            "office sit empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#1P#023FSpeaking of the old mayor...\x02\x03",

            "Weren't you and Joshua involved\x01",
            "in bringing him to justice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1016FHaha, yeah, kind of...\x02\x03",

            "#1008FWe got involved in an investigation\x01",
            "which led us right to his doorstep.\x02\x03",

            "The one who really arrested him was Lt. Schwarz\x01",
            "of the Royal Guard, though, after Kloe called her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x103,
        (
            "#1P#021FC'mon! You needn't be so humble.\x02\x03",

            "You were crucial in his arrest, I heard.\x01",
            "You make your teacher proud, honey.\x02\x03",

            "#020FBut I see...\x02\x03",

            "So that's how you met the princess?\x01",
            "I had been curious about the details\x01",
            "of THAT...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1000FYeah, Joshua and I helped out\x01",
            "with the Jenis school festival.\x02\x03",

            "#1015FY'know, I haven't seen Kloe since\x01",
            "the birthday festival...or Olivier,\x01",
            "I guess. For better or worse.\x02\x03",

            "#1003FAnd not just them... Tita, too...and Zin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x103,
        (
            "#1P#020FZin returned to Calvard after\x01",
            "the birthday celebrations.\x02\x03",

            "I believe a request came in from\x01",
            "the Calvard national guild office...\x02\x03",

            "He did say to give you his best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1007FI see... If it's work, it's work, I guess.\x02\x03",

            "#1025FHe helped us out a lot... I wish\x01",
            "I could've said goodbye, at least...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        (
            "#1P#020FYou'll meet him again someday, I'm sure.\x02\x03",

            "Oh, as for Tita and Professor Russell...\x02\x03",

            "Cassius and I explained the situation\x01",
            "to them after you left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1025FOh, I see... Thanks, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#1P#021FIt waaas adorable...\x01",
            "Tita's such a nice, earnest girl.\x02\x03",

            "#027FWe told her everything, and then,\x01",
            "her eyes filled with tears as though\x01",
            "she was just barely holding it in...\x02\x03",

            "She said, 'Estelle's working so hard, I can't\x01",
            "just sit here and cry! She taught me that!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1008FAhaha...\x02\x03",

            "#1013FOh, Tita...\x02\x03",

            "#1027FC'mon, Schera...\x01",
            "You're gonna make ME cry, here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#1P#021FHeehee! Sorry, sorry.\x02\x03",

            "#027FReally, though...you met some amazing\x01",
            "people over the course of your travels...\x01",
            "some really amazing friends.\x02\x03",

            "I hope you realize just how precious that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1012FYeah... I do.\x02\x03",

            "#1017FSay, Schera?\x02\x03",

            "When we get to Ruan, do you think we\x01",
            "could find time to go see everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#1P#021FOf course! We'll make the time.\x02\x03",

            "#020FSpeaking of time...we've still\x01",
            "got some before we arrive.\x02\x03",

            "I think I'll lounge these terribly creaky,\x01",
            "oh-so-ancient bones of mine in my seat.\x01",
            "Did you have any plans?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015FHmmmm...\x02\x03",

            "#1011FI think I'll just look around the ship\x01",
            "a bit. You can go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#1P#020FAll right, then.\x02\x03",

            "Just don't get so carried away that\x01",
            "you don't get off at Ruan, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 315, 400)

    def lambda_1F1F():
        OP_6D(1540, 5000, -2430, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1F1F)

    def lambda_1F37():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1F37)

    def lambda_1F47():

        label("loc_1F47")

        TurnDirection(0x101, 0x103, 0)
        OP_48()
        Jump("loc_1F47")

    QueueWorkItem2(0x101, 0, lambda_1F47)
    OP_8E(0x103, 0xFFFFFFE2, 0x13EC, 0xFFFFF9A2, 0x7D0, 0x0)
    OP_8C(0x103, 14, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x0)
    OP_8E(0x103, 0xFFFFFFE2, 0x13EC, 0x10E, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_44(0x101, 0x0)
    OP_71(0x0, 0x800)
    RemoveParty(0x2, 0xFF)

    label("loc_1FC3")

    OP_A2(0x1205)
    Fade(1000)
    EventEnd(0x0)
    Return()

    # Function_6_6BA end

    def Function_7_1FCE(): pass

    label("Function_7_1FCE")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_204A"),
        (1, "loc_2050"),
        (SWITCH_DEFAULT, "loc_2056"),
    )


    label("loc_204A")

    OP_A2(0x1200)
    Jump("loc_2056")

    label("loc_2050")

    OP_A2(0x1201)
    Jump("loc_2056")

    label("loc_2056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2064")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2068")

    label("loc_2064")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2068")

    Return()

    # Function_7_1FCE end

    SaveToFile()

Try(main)
