from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C2219_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_2093",         # 01, 1
        "Function_2_2175",         # 02, 2
        "Function_3_22ED",         # 03, 3
        "Function_4_2431",         # 04, 4
        "Function_5_2579",         # 05, 5
        "Function_6_27BB",         # 06, 6
        "Function_7_2956",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1592")
    OP_8C(0xFE, 270, 0)
    OP_4A(0xFE, 0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -1410, 0, 201500, 270)
    SetChrPos(0xF7, -1250, 0, 202500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x104, 0, 0, 201500, 270)
    SetChrPos(0x105, 250, 0, 202500, 270)
    Jump("loc_176")

    label("loc_124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_157")
    SetChrPos(0x104, 0, 0, 201500, 270)
    SetChrPos(0x127, 250, 0, 202500, 270)
    Jump("loc_176")

    label("loc_157")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176")
    SetChrPos(0x109, 125, 0, 202000, 270)

    label("loc_176")

    OP_6D(-1660, 0, 202610, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0xFE,
        "Mmmmph! Still hurts a bit, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "No use. Can't strain m'self any further.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_222")
    OP_A2(0xA)
    Jump("loc_225")

    label("loc_222")

    OP_A3(0xA)

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Cleared either 'Lighthouse Monster Hunt' or 'Maintenance Bag Delivery' quests in FC\x01",      # 0
            "Cleared neither\x01",                                                                          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    OP_A2(0xA)
    Jump("loc_2D4")

    label("loc_2D1")

    OP_A3(0xA)

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_538")

    ChrTalk(    #2
        0x101,
        "#1001FHi, Mr. Vogt! It's been a while!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #3
        0xFE,
        "Well, it's you bracer kids again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Still full o' vim and vinegar, I see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_481")

    ChrTalk(    #5
        0x106,
        (
            "#051FOh, yeah, now I remember.\x02\x03",

            "You were knocked out during that whole\x01",
            "mess with the Intelligence goons.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #6
        0x101,
        "#1001FYeah, this is Mr. Vogt, the lighthouse keeper.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #7
        0x101,
        (
            "#1000FHow are you these days, Mr. Vogt?\x01",
            "Still hanging in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_535")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_535")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #8
        0x103,
        "#023FYou've met before?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #9
        0x101,
        "#1000FUh-huh. You could say some stuff happened.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #10
        0x101,
        (
            "#1000FHow are you these days, Mr. Vogt?\x01",
            "Still hanging in there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_535")

    Jump("loc_82B")

    label("loc_538")


    ChrTalk(    #11
        0x101,
        "#1000FHi, Mr. Vogt! It's been a while!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #12
        0xFE,
        "Hmm? Who're you again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1016FOh, right. I guess you don't\x01",
            "really remember us, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6B1")

    ChrTalk(    #14
        0x106,
        (
            "#051FOh, yeah, this guy.\x02\x03",

            "He was knocked out during that whole\x01",
            "mess with the Intelligence goons.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #15
        0x101,
        "#1000FYeah, this is Mr. Vogt, the lighthouse keeper.\x02",
    )

    CloseMessageWindow()
    Jump("loc_733")

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_733")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        "#023FYou've met before?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1015FUh-huh. We chased some Intelligence\x01",
            "guys here on a job a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_733")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #18
        0xFE,
        (
            "Ah, that's it. You're those young\x01",
            "whippersnappers who showed up back\x01",
            "when I got knocked out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #19
        0x101,
        (
            "#1006FYeah, we're bracers. Well, I guess\x01",
            "we were junior bracers at the time.\x02\x03",

            "So how are you these days, Mr. Vogt?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B")


    ChrTalk(    #20
        0xFE,
        (
            "I've been all right, mostly.\x01",
            "Though recently I--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #21
        0xFE,
        "...Ah! Agh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)

    ChrTalk(    #22
        0x101,
        (
            "#1004FH-Hey! What's wrong?\x02\x03",

            "Are you all right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It's my bum back. Can't seem to shake\x01",
            "this pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Any time I bend at all, it's like someone's\x01",
            "drivin' a spike through my spine!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_98E")

    ChrTalk(    #25
        0x105,
        "#043FThat's awful...\x02",
    )

    CloseMessageWindow()

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9C1")

    ChrTalk(    #26
        0x106,
        "#052F#4POof. Sounds pretty painful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F8")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9F8")

    ChrTalk(    #27
        0x103,
        "#022F#4PDefinitely doesn't sound pleasant.\x02",
    )

    CloseMessageWindow()

    label("loc_9F8")


    ChrTalk(    #28
        0x101,
        (
            "#1015FCan't you take some medicine for\x01",
            "that or anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I've been dealin' with this pain since\x01",
            "you were in diapers, I'll have ya know!\x01",
            "I'll not waste time trying to cure it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "It'll go away on its own. I'll see to that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Unfortunately, I can't afford t' sit around\x01",
            "resting for too long right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1011FHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Is there something you need done?\x01",          # 0
            "...Well, take care of yourself, okay?\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC2")
    OP_28(0x6B, 0x4, 0x40)
    OP_A2(0x0)

    ChrTalk(    #33
        0x101,
        "#1000FDo take care of yourself, okay?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_C6E")

    ChrTalk(    #34
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Hmph. Still ain't got the faintest\x01",
            "idea how to care for others, do ya?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF")

    label("loc_C6E")


    ChrTalk(    #36
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Hmph. Really, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "You modern bracers are so callow.\x01",
            "Not like back in my day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF")


    ChrTalk(    #39
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "Oh, nothing. Nothing at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "...Bit foolish o' me, anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I been talking too long, when\x01",
            "I've got work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Good luck to you in your own work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1006FYeah, you too. Take care, old man!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    OP_4B(0xFE, 0)
    Jump("loc_1582")

    label("loc_DC2")

    OP_28(0x6B, 0x4, 0x2)
    OP_28(0x6B, 0x4, 0x4)
    OP_28(0x6B, 0x4, 0x8)
    OP_65(0x0, 0x1)

    ChrTalk(    #45
        0x101,
        "#1015FIs there something you need done?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Matter of fact, there is. I was right\x01",
            "in the middle of an important job when\x01",
            "you stormed in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "You know there are orbments used in\x01",
            "the lighthouse, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I swapped the parts out for new ones,\x01",
            "but I ain't given them all a test yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007FOh, that sounds like it could be a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Nah, no worries. This is my responsibility.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Wouldn't be much of a lighthouse keeper\x01",
            "if I asked someone else to do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I'll just take it slow an' easy.\x01",
            "And keep my back straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1003FI see...\x02\x03",

            "#1002FWell, don't strain yourself, okay?\x01",
            "You don't want to make it worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "You don't need to worry on that score,\x01",
            "little miss. I know my body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "...Ah, listen to me go on!\x01",
            "Sorry to chew your ears off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "Good luck with your work, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006FThanks!\x02\x03",

            "Take care, Mr. Vogt.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_1136():
        OP_8C(0x0, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1136)
    Sleep(100)

    def lambda_1149():
        OP_8C(0x1, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1149)
    Sleep(50)

    def lambda_115C():
        OP_8C(0x2, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_115C)
    Sleep(100)

    def lambda_116F():
        OP_8C(0x3, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_116F)
    Sleep(400)

    def lambda_1182():
        OP_94(0x1, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1182)
    Sleep(50)

    def lambda_119D():
        OP_94(0x1, 0x1, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_119D)

    def lambda_11B3():
        OP_94(0x1, 0x2, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_11B3)
    Sleep(50)

    def lambda_11CE():
        OP_94(0x1, 0x3, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_11CE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #58
        0xFE,
        "...Oh, yes, one moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "I almost forgot.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    def lambda_1235():
        OP_8C(0x0, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1235)
    Sleep(100)

    def lambda_1248():
        OP_8C(0x1, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1248)
    Sleep(50)

    def lambda_125B():
        OP_8C(0x2, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_125B)
    Sleep(100)

    def lambda_126E():
        OP_8C(0x3, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_126E)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #60
        0x101,
        "#1000FHmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "Well, about testing them orbments...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 315, 400)

    ChrTalk(    #62
        0xFE,
        (
            "There's a manual on the bookshelf there\x01",
            "with details on how to do it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #63
        0xFE,
        "If you're curious, feel free to take a look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1004FHuh?\x02\x03",

            "#1016FOh, uh, sure, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "It's an important job, to be sure, but\x01",
            "it's mostly just flippin' switches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Anyone could do it if they read the\x01",
            "manual, I reckon.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        (
            "#1019F(You know. D'you think, just maybe...?)\x02\x03",

            "(...he's being the most passive-aggressive\x01",
            "old fart in the universe and asking us to\x01",
            "help him out?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1501")

    ChrTalk(    #68
        0x106,
        "#551F(Ain't no 'maybe' about it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1540")

    label("loc_1501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1540")

    ChrTalk(    #69
        0x103,
        "#025F(There's not really a 'maybe' involved here.)\x02",
    )

    CloseMessageWindow()

    label("loc_1540")


    ChrTalk(    #70
        0xFE,
        "Mmm? Somethin' wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1016FNo, nothing!\x02\x03",

            "Well, see ya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1582")

    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    OP_4B(0xFE, 0)
    Jump("loc_2092")

    label("loc_1592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15E3")
    TalkBegin(0xFE)

    ChrTalk(    #72
        0xFE,
        "Hmph, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Kids these days can't hear worth a darn.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2092")

    label("loc_15E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16AB")
    TalkBegin(0xFE)

    ChrTalk(    #74
        0xFE,
        "Ah, you've done me a good turn again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Can't help but feel like I'm more an'\x01",
            "more of a bother on you young folk\x01",
            "these days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I really am startin' to get old,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2092")

    label("loc_16AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_17FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A4")

    ChrTalk(    #77
        0xFE,
        "Mmmmmmph. This is maddening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "There's not a blasted thing wrong with it,\x01",
            "but the lighthouse just won't work at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Zack might have a point...\x01",
            "Maybe it is a little more serious\x01",
            "than I been givin' it credit for.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_17FA")

    label("loc_17A4")


    ChrTalk(    #80
        0xFE,
        "Mmmmmmph. This is maddening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "There really might be a bigger problem here...\x02",
    )

    CloseMessageWindow()

    label("loc_17FA")

    Jump("loc_208F")

    label("loc_17FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1923")

    ChrTalk(    #82
        0xFE,
        (
            "That callow, loudmouthed kid needs to keep\x01",
            "his untrained opinions out of my business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I know this lighthouse better than anyone,\x01",
            "I say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "The cause of this is somewhere in the\x01",
            "internal mechanics!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I can fix something this simple in no time.\x01",
            "Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1990")

    label("loc_1923")


    ChrTalk(    #86
        0xFE,
        (
            "Hmph. That boy needs to learn when\x01",
            "to shut up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I know this lighthouse better than anyone,\x01",
            "I say!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1990")

    Jump("loc_208F")

    label("loc_1993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A0D")

    ChrTalk(    #88
        0xFE,
        "The manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "If you're curious, feel free to have a look.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B69")

    label("loc_1A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A87")

    ChrTalk(    #90
        0xFE,
        (
            "Portos knows how important this\x01",
            "lighthouse is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I think I can trust him to find\x01",
            "me a proper successor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B69")

    label("loc_1A87")

    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        "Wonder who'll be the next mayor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Personally, I'm hopin' Portos wins.\x01",
            "Man's got a good head on his shoulders!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B69")

    ChrTalk(    #94
        0xFE,
        "Anyway, the manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()

    label("loc_1B69")

    Jump("loc_208F")

    label("loc_1B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BDF")

    ChrTalk(    #96
        0xFE,
        "The manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C83")

    ChrTalk(    #98
        0xFE,
        (
            "Lighthouse keepin' isn't something just\x01",
            "anyone can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I'd love to meet some young fella who\x01",
            "wants to take on the role after I'm in\x01",
            "the ground!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1C83")

    OP_A2(0x2)

    ChrTalk(    #100
        0xFE,
        (
            "A lighthouse keeper's job is a lonely one,\x01",
            "but it's important if we want to keep the\x01",
            "coast safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Only someone who's willing to make\x01",
            "sacrifices for the safety of others\x01",
            "can do it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DA9")

    ChrTalk(    #102
        0xFE,
        "Anyway, the manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()

    label("loc_1DA9")

    Jump("loc_208F")

    label("loc_1DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E23")

    ChrTalk(    #104
        0xFE,
        "The manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F31")

    label("loc_1E23")

    OP_A2(0x2)

    ChrTalk(    #106
        0xFE,
        (
            "Suppose my years are starting to catch\x01",
            "up to me... Only natural my back should\x01",
            "start to give out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Hope I can find an apprentice for the\x01",
            "lighthouse soon...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F31")

    ChrTalk(    #108
        0xFE,
        "Anyway, the manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()

    label("loc_1F31")

    Jump("loc_208F")

    label("loc_1F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_208F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA7")

    ChrTalk(    #110
        0xFE,
        "The manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()
    Jump("loc_208F")

    label("loc_1FA7")

    OP_A2(0x2)

    ChrTalk(    #112
        0xFE,
        (
            "Phew! Can't hardly work at all with\x01",
            "my back in this state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Suppose I do need to get around to\x01",
            "findin' a successor...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_208F")

    ChrTalk(    #114
        0xFE,
        "Anyway, the manual's on the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Give it a read, if you're interested!\x02",
    )

    CloseMessageWindow()

    label("loc_208F")

    TalkEnd(0xFE)

    label("loc_2092")

    Return()

    # Function_0_AA end

    def Function_1_2093(): pass

    label("Function_1_2093")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #116
        "\x07\x05There's a book on the shelf titled 'Lighthouse Manual.'\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Book\x01",       # 0
            "Don't Read\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2171")
    OP_B8(0x231, 0x0)
    OP_28(0x6B, 0x1, 0x1)
    OP_28(0x6B, 0x1, 0x8000)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)

    label("loc_2171")

    TalkEnd(0xFF)
    Return()

    # Function_1_2093 end

    def Function_2_2175(): pass

    label("Function_2_2175")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #117 op#5
        "Activation Switch\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_21D7")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "★[ON]\x01",       # 0
            "  [OFF]\x01",      # 1
            "Stop\x01",         # 2
        )
    )

    Jump("loc_21F4")

    label("loc_21D7")


    Menu(
        0,
        -1,
        155,
        1,
        (
            "  [ON]\x01",       # 0
            "★[OFF]\x01",      # 1
            "Stop\x01",         # 2
        )
    )


    label("loc_21F4")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224D")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9E, 0x1, 0x5A)

    label("loc_224D")

    OP_A2(0x3)
    Jump("loc_22BF")

    label("loc_2253")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9E, 0x0, 0x5A)
    Sleep(1000)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BF")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x05Error! Start-up failed!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_22BF")

    Jump("loc_22E9")

    label("loc_22C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22E3")
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_23(0x9E)

    label("loc_22E3")

    OP_A3(0x8)
    OP_A3(0x3)

    label("loc_22E9")

    TalkEnd(0xFF)
    Return()

    # Function_2_2175 end

    def Function_3_22ED(): pass

    label("Function_3_22ED")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #119 op#5
        "Orbal Amplitude\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2357")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "★[HIGH]\x01",      # 0
            "　[MID]\x01",       # 1
            "　[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )

    Jump("loc_23AF")

    label("loc_2357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2388")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "　[HIGH]\x01",      # 0
            "　[MID]\x01",       # 1
            "★[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )

    Jump("loc_23AF")

    label("loc_2388")


    Menu(
        0,
        -1,
        155,
        1,
        (
            "　[HIGH]\x01",      # 0
            "★[MID]\x01",       # 1
            "　[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )


    label("loc_23AF")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EF")
    OP_22(0x64, 0x0, 0x64)
    OP_A2(0x4)
    OP_A3(0x5)
    Jump("loc_2429")

    label("loc_23EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240A")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x4)
    OP_A3(0x5)
    Jump("loc_2429")

    label("loc_240A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2425")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x4)
    OP_A2(0x5)
    Jump("loc_2429")

    label("loc_2425")

    TalkEnd(0xFF)
    Return()

    label("loc_2429")

    Call(1, 6)
    TalkEnd(0xFF)
    Return()

    # Function_3_22ED end

    def Function_4_2431(): pass

    label("Function_4_2431")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #120 op#5
        "Stabilizer Strength\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_249F")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "★[HIGH]\x01",      # 0
            "　[MID]\x01",       # 1
            "　[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )

    Jump("loc_24F7")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_24D0")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "　[HIGH]\x01",      # 0
            "　[MID]\x01",       # 1
            "★[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )

    Jump("loc_24F7")

    label("loc_24D0")


    Menu(
        0,
        -1,
        155,
        1,
        (
            "　[HIGH]\x01",      # 0
            "★[MID]\x01",       # 1
            "　[LOW]\x01",       # 2
            "Stop\x01",          # 3
        )
    )


    label("loc_24F7")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2537")
    OP_22(0x64, 0x0, 0x64)
    OP_A2(0x6)
    OP_A3(0x7)
    Jump("loc_2571")

    label("loc_2537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2552")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x6)
    OP_A3(0x7)
    Jump("loc_2571")

    label("loc_2552")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256D")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x6)
    OP_A2(0x7)
    Jump("loc_2571")

    label("loc_256D")

    TalkEnd(0xFF)
    Return()

    label("loc_2571")

    Call(1, 6)
    TalkEnd(0xFF)
    Return()

    # Function_4_2431 end

    def Function_5_2579(): pass

    label("Function_5_2579")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 0, -1, -1)

    AnonymousTalk(    #121 op#5
        "Connection Quartz\x05\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_25DB")

    Menu(
        0,
        -1,
        155,
        1,
        (
            "★[ON]\x01",       # 0
            "  [OFF]\x01",      # 1
            "Stop\x01",         # 2
        )
    )

    Jump("loc_25F8")

    label("loc_25DB")


    Menu(
        0,
        -1,
        155,
        1,
        (
            "　[ON]\x01",       # 0
            "★[OFF]\x01",      # 1
            "Stop\x01",         # 2
        )
    )


    label("loc_25F8")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_56(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A2")
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26B7")
    OP_A2(0x8)
    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0xA1, 0x1, 0x64)
    OP_23(0x9E)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #122
        0x101,
        "#1004FWaah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C2209   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_279F")

    label("loc_26B7")

    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2737")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #123
        (
            "\x07\x05Error! Output insufficient!\x01",
            "Ceasing boot sequence!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_279C")

    label("loc_2737")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #124
        (
            "\x07\x05Control system destabilizing!\x01",
            "Ceasing boot sequence!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_279C")

    OP_A3(0x3)

    label("loc_279F")

    Jump("loc_27B7")

    label("loc_27A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B7")
    OP_22(0x64, 0x0, 0x64)
    OP_A3(0x8)

    label("loc_27B7")

    TalkEnd(0xFF)
    Return()

    # Function_5_2579 end

    def Function_6_27BB(): pass

    label("Function_6_27BB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_27ED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_280B")

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2801")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_280B")

    label("loc_2801")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_280B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_281F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_283D")

    label("loc_281F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2833")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_283D")

    label("loc_2833")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_283D")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28C9")
    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    OP_A3(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #125
        (
            "\x07\x05Error! Output is zero!\x01",
            "Ceasing boot sequence!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_28C9")

    Jump("loc_2955")

    label("loc_28CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2955")
    Sleep(400)
    OP_23(0x9E)
    OP_22(0xE1, 0x0, 0x64)
    OP_A3(0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        (
            "\x07\x05Control system destabilizing!\x01",
            "Ceasing boot sequence!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2955")

    Return()

    # Function_6_27BB end

    def Function_7_2956(): pass

    label("Function_7_2956")

    EventBegin(0x0)
    OP_28(0x6B, 0x1, 0x2)
    OP_6D(-1670, 0, 199940, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 0)
    OP_8C(0x8, 180, 0)
    OP_22(0xA1, 0x1, 0x64)
    SetChrPos(0x101, -3090, 0, 199520, 0)
    SetChrPos(0xF7, -2130, 0, 199060, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A00")
    SetChrPos(0x104, -2150, 0, 197690, 0)
    SetChrPos(0x105, -3300, 0, 198050, 0)
    Jump("loc_2A52")

    label("loc_2A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A33")
    SetChrPos(0x104, -2150, 0, 197690, 0)
    SetChrPos(0x127, -3300, 0, 198050, 0)
    Jump("loc_2A52")

    label("loc_2A33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A52")
    SetChrPos(0x109, -2725, 0, 197870, 0)

    label("loc_2A52")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #127
        0x8,
        "Ah, you did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1015F#7PSo, um, we can just leave it\x01",
            "alone now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        "You can. It's in diagnostic mode.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "It'll stop on its own in a little while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1011F#7POkay, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        "Still! I'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "You managed to figure out with\x01",
            "nothin' more than the manual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1016F#7PHaha... It wasn't easy, to be honest.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_23(0xA1)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #135
        0x101,
        (
            "#1004FOh, hey!\x02\x03",

            "#1015FLooks like it stopped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "Yes, indeed. The diagnostic's done,\x01",
            "and there were no problems to report.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2CD8")

    ChrTalk(    #137
        0x8,
        (
            "So I've made you kids take care of me again\x01",
            "for nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "Sorry to put you through all this trouble.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D47")

    label("loc_2CD8")


    ChrTalk(    #139
        0x8,
        (
            "It's been mighty neighborly of you to do\x01",
            "all this for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "Sorry to put you through all this trouble.\x02",
    )

    CloseMessageWindow()

    label("loc_2D47")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #141
        0x101,
        "#1001F#7PNo, it's fine!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DCB")

    ChrTalk(    #142
        0x106,
        (
            "#051F#4PYeah, no need to thank us. Just make\x01",
            "sure you take it easy on your back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2E20")

    ChrTalk(    #143
        0x103,
        (
            "#021F#4PYes, no thanks are necessary.\x01",
            "Just take care of your back, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E20")


    ChrTalk(    #144
        0x8,
        (
            "No, no, no. I can't let you go without\x01",
            "expressing a little bit of my gratitude!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        "Here.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #146
        "\x07\x00Received #987i x 5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #147
        "\x07\x00Received #988i x 5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3DB, 5)
    OP_3E(0x3DC, 5)

    ChrTalk(    #148
        0x101,
        "#1011F#7POh... These are, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        "Some bait for sea fishin'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "You can land some real whoppers on\x01",
            "the cliffs near the lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        "You should try, if you've got the time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1001F#7PAww, thanks!\x02\x03",

            "#1015FAnyway, we should get moving along, but...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Take care, old man!\x01",                   # 0
            "Anything else we can do for you?\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3140")

    ChrTalk(    #153
        0x101,
        "#1000F#7PTake care, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        "Mmm. Yes, I'll take care...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "Would've been nice to see a little\x01",
            "more care from you, perhaps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "But, ah well... Till we meet again,\x01",
            "ya whippersnappers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C5")

    label("loc_3140")


    ChrTalk(    #157
        0x101,
        "#1000F#7PDid you need anything else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "I've got all I need, little miss.\x01",
            "However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "...it's good of you to ask.\x01",
            "Very, very important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "It shows that you have a heart that\x01",
            "cares for others, as any modern bracer\x01",
            "should. Just like the bracers of old...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1001F#7PAhaha! Well, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "You make sure and remember\x01",
            "that attitude, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        "Now, safe travels!\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6B, 0x1)
    OP_2C(0x6B, 0x1F4)

    label("loc_32C5")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #164
        "Quest #2C[Lighthouse Test Run] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x6B, 0x4, 0x10)
    OP_A2(0x1)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    EventEnd(0x0)
    OP_8C(0x8, 270, 0)
    OP_4B(0x8, 0)
    Return()

    # Function_7_2956 end

    SaveToFile()

Try(main)
