from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1101_1 ._SN',
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
        "Function_1_1E2",          # 01, 1
        "Function_2_330",          # 02, 2
        "Function_3_58A",          # 03, 3
        "Function_4_ECF",          # 04, 4
        "Function_5_1EF3",         # 05, 5
        "Function_6_2418",         # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xA)"), scpexpr(EXPR_END)), "loc_104")
    Call(1, 1)
    Jump("loc_1DB")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x11)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 2)
    Jump("loc_1DB")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_185")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1DB")

    label("loc_185")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1DB")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_269")

    ChrTalk(    #2
        0xA,
        (
            "Hrmmmmm, blast it all.\x01",
            "I'm sure I've seen the girl in\x01",
            "that photo of yours, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        "Now if only I could place her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_32C")

    label("loc_269")


    ChrTalk(    #4
        0xA,
        "Say, this photo of yours...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1004FExcuse me, sir, but do you know this girl?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #6
        0xA,
        "Hrmmmmm... Feel like I do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "There's something I just can't place,\x01",
            "though... Sorry, kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_32C")

    TalkEnd(0xA)
    Return()

    # Function_1_1E2 end

    def Function_2_330(): pass

    label("Function_2_330")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_444")

    ChrTalk(    #8
        0x11,
        (
            "I think your best clues will be hair\x01",
            "and eye color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "Other outward physical signs or mannerisms\x01",
            "change as people grow older, and you're\x01",
            "working on a decade here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "Discard any expectations or biases you\x01",
            "may have. Focus on the constants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57F")

    label("loc_444")


    ChrTalk(    #11
        0x11,
        "So you're trying to find someone, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "I think your best clues will be hair\x01",
            "and eye color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "Other outward physical signs or mannerisms\x01",
            "change as people grow older, and you're\x01",
            "working on a decade here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "Discard any expectations or biases you\x01",
            "may have. Focus on the constants.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_57F")

    Jump("loc_586")

    label("loc_582")

    Call(0, 12)

    label("loc_586")

    TalkEnd(0x11)
    Return()

    # Function_2_330 end

    def Function_3_58A(): pass

    label("Function_3_58A")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 33010, 0, 74070, 180)
    SetChrPos(0x9, 33850, 0, 74840, 180)
    OP_4A(0xE, 255)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_6D(48680, 0, 82940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)

    def lambda_613():
        OP_67(0, 7520, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_613)

    def lambda_62B():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62B)

    def lambda_63B():
        OP_6C(359000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_63B)

    def lambda_64B():
        OP_8E(0x8, 0x80F2, 0x0, 0x10338, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64B)
    Sleep(150)

    def lambda_66B():
        OP_8E(0x9, 0x843A, 0x0, 0x1063A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_66B)
    OP_6D(33430, 0, 67300, 6000)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x3)
    Sleep(400)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #16
        0x8,
        "#610FSay, Lila?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #17
        0x9,
        "#620FYes, Miss Maybelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#610FAbout what we were discussing earlier...\x02\x03",

            "When were you planning on doing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#620FMy trip back to Leman, you mean?\x02\x03",

            "I haven't quite decided yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#610FAll right.\x02\x03",

            "Just be sure and let me know when\x01",
            "you're going well in advance, okay?\x02\x03",

            "I'll need to adjust my schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#622FWhat do you mean, Miss Maybelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#610FWell, I AM going with you, after all.\x02\x03",

            "I really want to see what your home\x01",
            "was like.\x02\x03",

            "Besides...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        "#624FBesides what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#610FI was thinking, it would be really nice\x01",
            "to hear some stories from your childhood.\x02\x03",

            "I know you've heard all sorts of stories\x01",
            "about me from before you came to live\x01",
            "here.\x02\x03",

            "And I need to find some kind of embarrassing\x01",
            "chink in that armor of yours, or I won't be\x01",
            "able to do ANYTHING with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#621FSo you're after my naughtiest secrets?\x01",
            "Haha...\x02\x03",

            "#620FAhem, well. I'm afraid I shall have to\x01",
            "disappoint you, Miss Maybelle. My early\x01",
            "childhood was one of exquisite conduct.\x02\x03",

            "Unlike certain infamous tomboys who would be\x01",
            "scandalized should their pasts be made public,\x01",
            "I have nothing to fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#611FOhhh, reeeeeeeeally?\x02\x03",

            "I wouldn't underestimate my ability to\x01",
            "sniff out the truth, if I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "#621FHahaha...\x01",
            "Well, let's see what you can manage.\x02\x03",

            "I'll let you know as soon as I've made\x01",
            "a decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#610FPlease do, Lila.\x02\x03",

            "Anyway, what's on the agenda for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#620FYou have your regularly scheduled\x01",
            "meetings inside the manor from morning\x01",
            "until teatime.\x02\x03",

            "Afterward, you will attend the review\x01",
            "board for applicants to the market.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x8,
        (
            "#613FWait, the review board?\x01",
            "That's TODAY?!\x02\x03",

            "Oh, Aidios, just strike me dead. I have to\x01",
            "read those applicant evaluations right\x01",
            "away!\x02\x03",

            "#614FLila, hurry!\x01",
            "We've gotta move it!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA0():

        label("loc_DA0")

        TurnDirection(0x9, 0x8, 400)
        OP_48()
        Jump("loc_DA0")

    QueueWorkItem2(0x9, 1, lambda_DA0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x80F2, 0x0, 0xE678, 0x1388, 0x0)

    ChrTalk(    #31
        0x9,
        (
            "#623F#6POh, goodness...\x02\x03",

            "Something tells me I won't be going to\x01",
            "Leman for a while...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0x1)

    def lambda_E35():
        OP_8E(0x9, 0x843A, 0x0, 0xE678, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E35)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_6D(36200, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)
    EventEnd(0x0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_4B(0xA, 255)
    OP_4B(0xE, 255)
    Return()

    # Function_3_58A end

    def Function_4_ECF(): pass

    label("Function_4_ECF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE5")
    TurnDirection(0x4, 0xD, 0)

    label("loc_EE5")

    Fade(1000)
    EventBegin(0x0)
    OP_6D(47700, 0, 47800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF6, 48200, 0, 48120, 90)
    SetChrPos(0xF7, 48100, 0, 47360, 90)
    SetChrPos(0xF8, 47200, 0, 48130, 90)
    SetChrPos(0xF9, 47100, 0, 47320, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8A")
    SetChrPos(0x4, 46150, 0, 47720, 90)

    label("loc_F8A")

    OP_0D()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)
    TurnDirection(0xD, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(    #32
        0xD,
        "Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F#6PHey. Sorry about before.\x01",
            "Didn't really get to say hi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        "No, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        "I gather you're awful busy with work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1006F#6PYou could say that.\x02\x03",

            "Are you here in Bose on work yourself?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1441")

    label("loc_109E")


    ChrTalk(    #37
        0xD,
        "Hey...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(    #38
        0x101,
        (
            "#1004F#6POh... You were in Manoria last, right?\x02\x03",

            "#1000FSo you're in Bose now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1441")

    label("loc_110A")


    ChrTalk(    #39
        0x101,
        (
            "#1004F#6PWait, I know you. Orvid, right?\x02\x03",

            "#1001FWow, it feels like it's been forever!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1199")

    ChrTalk(    #40
        0x106,
        "#052FSomeone you know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_1241")

    label("loc_1199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D1")

    ChrTalk(    #41
        0x103,
        "#023FOh, someone you know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_1241")

    label("loc_11D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1207")

    ChrTalk(    #42
        0x108,
        "#070FYou know him, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_1241")

    label("loc_1207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1241")

    ChrTalk(    #43
        0x104,
        "#030FAn acquaintance, I assume?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1380")

    ChrTalk(    #44
        0x101,
        (
            "#1000F#6PYeah, Orvid's a merchant who gets\x01",
            "really toxic, er, rare ingredients.\x02\x03",

            "#1007FAh, but this is no time for introductions.\x02\x03",

            "We need to get to Ravennue, pronto!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        "You seem to be under some pressure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "Don't let me keep you!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #47
        0x101,
        "#1002F#6PYeah, sorry. Pardon us!\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0xD, 0, 0)
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_1380")


    ChrTalk(    #48
        0x101,
        (
            "#1000FYeah, Orvid's a merchant who gets\x01",
            "really toxic, er, rare ingredients.\x02\x03",

            "I did a job for him a while back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #49
        0x101,
        (
            "#1011F#6PSo are you chasing the perfect ingredients\x01",
            "in Bose now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1441")


    ChrTalk(    #50
        0xD,
        "Yes, I'm coming to the end of a long road.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        (
            "My ultimate goal is to secure a deal\x01",
            "with the Anterose.\x02\x03",

            "The first step is going to be selling\x01",
            "some of my ingredients in the market...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        (
            "#1015F#6PUmm, I kinda feel like I missed something\x01",
            "again.\x02\x03",

            "So your goal's to sell stuff to the Anterose\x01",
            "restaurant...but first you're going to sell\x01",
            "in the market? Why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "If I could, I'd love to approach them directly.\x02\x03",

            "But they won't deal with anyone who lacks\x01",
            "an introduction from another more trusted\x01",
            "source.\x02\x03",

            "Given how famous they are, it's only\x01",
            "natural they'd be cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1004F#6PYeah, guess that's the Anterose for you.\x01",
            "They can be kind of...snooty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "So you're working in Bose at the\x01",
            "moment, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1015F#6PYeah, some...stuff happened.\x02\x03",

            "#1011FSpeaking of stuff, though...\x02\x03",

            "We actually have a job from the Anterose,\x01",
            "now that I think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1813")

    ChrTalk(    #57
        0x106,
        (
            "#050FYeah, we're collecting some ingredients\x01",
            "for 'em ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1944")

    label("loc_1813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_187E")

    ChrTalk(    #58
        0x103,
        (
            "#020FYes, we've gotten into the ingredient\x01",
            "collecting business ourselves, for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1944")

    label("loc_187E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CF")

    ChrTalk(    #59
        0x108,
        (
            "#070FYes. We're the ones collecting ingredients\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1944")

    label("loc_18CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(    #60
        0x104,
        (
            "#030FIndeed. Our charge is to find certain\x01",
            "ingredients for the rose of Bose.\x01",
            "Quite a coincidence!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1944")

    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0xD,
        (
            "WHAT?! Collecting ingredients?!\x02\x03",

            "And for the Anterose itself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F#6PYeah, it's been kind of a pain in the butt.\x02\x03",

            "They're looking for some REALLY weird stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "Hmmmmm! How interesting.\x02\x03",

            "What ingredients do you need,\x01",
            "out of pure, academic curiosity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1015F#6PUh, one sec.\x01",
            "I've got the list in my notebook...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05Estelle showed Orvid the list of ingredients from the\x01",
            "Anterose.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #66
        0xD,
        (
            "Ha-ha-ha! Is that really all?\x02\x03",

            "I carry this much with me\x01",
            "on a daily basis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1004F#6PWhaaaa?! Seriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C11")

    ChrTalk(    #68
        0x109,
        (
            "#1060FWell, hey!\x01",
            "How's that for some divine guidance?\x02\x03",

            "How about we take Aidios up on the help\x01",
            "and enlist Mr. Orvid's aid?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(    #69
        0x104,
        (
            "#030FWell! How utterly convenient.\x02\x03",

            "Beloved companions, why not enlist\x01",
            "the good Mr. Orvid's aid?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE4")

    ChrTalk(    #70
        0x108,
        (
            "#070FJust a bit of a coincidence, eh?\x02\x03",

            "Why don't we ask for his help?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D74")

    ChrTalk(    #71
        0x103,
        (
            "#020FWell, then! I'm not about to look\x01",
            "a gift horse in the mouth.\x02\x03",

            "Perhaps we can get a little help from\x01",
            "Mr. Orvid, here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1D74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD4")

    ChrTalk(    #72
        0x106,
        (
            "#051FHeh, you want to talk coincidences.\x02\x03",

            "How 'bout we help one another out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD4")


    ChrTalk(    #73
        0xD,
        (
            "I would ask it of you before you ask me!\x01",
            "This is perfect for both of us.\x02\x03",

            "I'll be happy to provide you with the\x01",
            "ingredients if you'll introduce me to\x01",
            "the manager of the Anterose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1017F#6PAll right.\x02\x03",

            "We can totally do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        "It's a deal, then!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1131   ._SN", 103, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0xD)
    Return()

    # Function_4_ECF end

    def Function_5_1EF3(): pass

    label("Function_5_1EF3")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 19300, 0, 48720, 135)
    SetChrPos(0x101, 20510, 0, 47110, 320)
    SetChrPos(0xF7, 21430, 0, 47400, 315)
    SetChrPos(0xF8, 21520, 0, 46030, 315)
    SetChrPos(0xF9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2000")

    ChrTalk(    #76
        0x12,
        "Are we all ready, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006FYes, sorry to keep you waiting, ma'am.\x02\x03",

            "Let's get going!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23EE")

    label("loc_2000")


    ChrTalk(    #78
        0x12,
        (
            "Ah, there you are!\x01",
            "I've been waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        "Shall we proceed, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006FWhenever you're ready, ma'am.\x02\x03",

            "Our goal is Ravennue Village, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2139")

    ChrTalk(    #81
        0x106,
        (
            "#050FYeah. We all know that road by now, but\x01",
            "don't forget, we're escorting a civvy.\x02\x03",

            "Let's avoid monsters along the road\x01",
            "as much as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231C")

    label("loc_2139")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #82
        0x103,
        (
            "#020FYes. I think we all know the road by now,\x01",
            "but remember, this time Ms. Mirano is\x01",
            "with us.\x02\x03",

            "We should avoid contact with monsters\x01",
            "whenever possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231C")

    label("loc_21E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(    #83
        0x108,
        (
            "#070FIndeed. We know the road, but don't forget\x01",
            "that we are escorting someone.\x02\x03",

            "We should avoid monsters when we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231C")

    label("loc_2273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231C")

    ChrTalk(    #84
        0x104,
        (
            "#030FIt is. The road is a familiar one, but\x01",
            "do not forget that this fair flower is\x01",
            "with us now.\x02\x03",

            "It would behoove us to avoid combat\x01",
            "wherever we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231C")


    ChrTalk(    #85
        0x12,
        (
            "Yes, quite so! What a waste of\x01",
            "time a fight would be, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "Why, keep me out of danger, and I may\x01",
            "just give you all a nice little bonus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1006FWe'll do our best, ma'am!\x02\x03",

            "#1018FLet's be off, then!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23EE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x7C, 0x1, 0x4)
    OP_28(0x7C, 0x4, 0x8)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    AddParty(0x46, 0xFF, 0xFF)
    NewScene("ED6_DT21/R1200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1EF3 end

    def Function_6_2418(): pass

    label("Function_6_2418")

    EventBegin(0x0)
    RemoveParty(0x46, 0xFF)
    SetChrPos(0x12, 19300, 0, 48720, 135)
    OP_4A(0x12, 255)
    SetChrPos(0x101, 20510, 0, 47110, 320)
    SetChrPos(0xF7, 21430, 0, 47400, 315)
    SetChrPos(0xF8, 21520, 0, 46030, 315)
    SetChrPos(0xF9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #88
        0x12,
        "Oh? Do you all need something in town?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1006FYes, sorry, ma'am, but we need a few\x01",
            "things.\x02\x03",

            "We'll be right back, so please wait\x01",
            "for us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        "As you wish. Do hurry, though!\x02",
    )

    CloseMessageWindow()
    OP_28(0x7C, 0x1, 0x4000)
    OP_28(0x7C, 0x3, 0x8)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x15), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2588")
    OP_28(0x7C, 0x1, 0x2000)

    label("loc_2588")

    OP_4B(0x12, 255)
    SetChrPos(0x12, 19300, 0, 48720, 180)
    EventEnd(0x0)
    Return()

    # Function_6_2418 end

    SaveToFile()

Try(main)
