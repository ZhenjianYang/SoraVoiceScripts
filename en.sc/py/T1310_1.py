from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1310_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1310_1 ._SN',
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
        "Function_1_2E1E",         # 01, 1
        "Function_2_2E38",         # 02, 2
        "Function_3_2E52",         # 03, 3
        "Function_4_2E69",         # 04, 4
        "Function_5_2EE3",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 82350, 0, 53600, 180)
    SetChrPos(0x106, 83210, 0, 53720, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x105, 82610, 0, 54630, 180)
    SetChrPos(0xF9, 81580, 0, 54720, 180)
    Jump("loc_159")

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137")
    SetChrPos(0x105, 82610, 0, 54630, 180)
    SetChrPos(0xF8, 81580, 0, 54720, 180)
    Jump("loc_159")

    label("loc_137")

    SetChrPos(0xF8, 82610, 0, 54630, 180)
    SetChrPos(0xF9, 81580, 0, 54720, 180)

    label("loc_159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_175")
    SetChrPos(0xC, 82940, 0, 52010, 0)

    label("loc_175")

    OP_4A(0xC, 255)
    OP_6D(82800, 0, 53860, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(35000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")
    OP_28(0x7A, 0x1, 0x8)

    ChrTalk(    #0
        0xC,
        "Phew! Glad I managed to get this far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        "Oh, but I can't stay here forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xC,
        (
            "I've got to figure out...SOME way to\x01",
            "get back to Jenis, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1004F#6P(Aha!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36A")

    ChrTalk(    #4
        0x105,
        (
            "#042F#6P(That's really Felicity.)\x02\x03",

            "#045F(I'll admit, I didn't think she'd make\x01",
            "it this far on her own...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x106,
        (
            "#050F#6P(A royal academy student...)\x02\x03",

            "(I'm guessing that's the runaway we're\x01",
            "looking for.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1002F#6P(Yeah.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EB")

    label("loc_36A")


    ChrTalk(    #7
        0x106,
        (
            "#050F#6P(Looks like a royal academy student...)\x02\x03",

            "(I'm guessing that's the runaway we're\x01",
            "looking for.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002F#6P(Yeah.)\x02",
    )

    CloseMessageWindow()

    label("loc_3EB")

    OP_8C(0xC, 0, 400)

    ChrTalk(    #9
        0xC,
        "#4POh, you are...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_544")

    ChrTalk(    #10
        0x101,
        (
            "#1016F#6PUh, hi, it's been a while!\x02\x03",

            "I guess it has, anyway. Haha, it's only\x01",
            "hit me just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xC,
        "#4POh! Yes, hello, it has!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xC,
        "#4PSince we last met at the academy, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        "#040F#6PHello, Felicity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        "#4PWha... Kloe, you're here too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        "#4PWhat on earth brings all of you out here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FA")

    label("loc_544")


    ChrTalk(    #16
        0x101,
        (
            "#1000F#6PUh, hi, it's been a while!\x02\x03",

            "I guess it has, anyway. Haha, it's only\x01",
            "hit me just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        "#4PSince we last met at the academy, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        "#4PWhat brings you here today?\x02",
    )

    CloseMessageWindow()

    label("loc_5FA")

    Jump("loc_64A")

    label("loc_5FD")


    ChrTalk(    #19
        0xC,
        "#4POh, hello again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "#4PDid you have some other business\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64A")


    ChrTalk(    #21
        0x101,
        (
            "#1000F#6PIf I can, I'd like to ask you something.\x02\x03",

            "#1015FWe're dealing with an emergency,\x01",
            "and we'd like your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        "#4PMy...cooperation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "#4PWith what, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F#6PIt's not hard or anything.\x02\x03",

            "#1002FWe just need you to come with us...\x01",
            "back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_96(0xC, 0x144C4, 0x0, 0xC8F0, 0x1F4, 0x2710)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")

    ChrTalk(    #25
        0x105,
        "#044F#6PFelicity?!\x02",
    )

    CloseMessageWindow()

    label("loc_7BA")


    ChrTalk(    #26
        0xC,
        "#4PYou... I knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "#4P#3SLet me guess...\x01",
            "You're Reina's hired thugs now!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#6PThugs? Uhhhh...\x02\x03",

            "I'd kinda like to not be compared to\x01",
            "surly guys with clubs, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B2")

    ChrTalk(    #29
        0x105,
        "#045F#6PYes, r-really...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_8B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DD")

    ChrTalk(    #30
        0x107,
        "#067FUmmm... Haha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_8DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_941")

    ChrTalk(    #31
        0x104,
        (
            "#035FAh, what a tragic mistake.\x02\x03",

            "I am an ally of fair maidens,\x01",
            "not their foe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BE")

    ChrTalk(    #32
        0x108,
        (
            "#070FHaha! Well, Agate and I are rather large\x01",
            "and imposing.\x02\x03",

            "I can see how she'd come to that\x01",
            "conclusion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BE")


    ChrTalk(    #33
        0x106,
        (
            "#551F#6PNow hang on, miss.\x01",
            "Figured that school would've taught this lesson.\x02\x03",

            "Bracers are sworn to neutrality in conflicts.\x01",
            "We're no one's thugs and no one's operatives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        (
            "#4PH-Hmph! Yes, I know what you are.\x01",
            "In theory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "#4PBut trust me, I know how the world REALLY\x01",
            "works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "#4PRegardless of pretty words, you intend to\x01",
            "drag me back by force, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        (
            "#057F#6PIf you try to flee into the dangerous\x01",
            "wilderness on your own, we may have to,\x01",
            "yes.\x02\x03",

            "This ain't a barrel of laughs for us, either.\x01",
            "Please, just cooperate and come with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x144C4, 0x0, 0xD016, 0x7D0, 0x0)
    TurnDirection(0x106, 0xC, 0)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xC, 0xB4, 0x64, 0x3E8, 0x0)

    ChrTalk(    #38
        0xC,
        "#4PSTAY BACK, YOU!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        "#4PAny closer and I'll scream!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1002F#6PFelicity, just...calm down a second.\x02\x03",

            "It's okay, we're not going to do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x106,
        (
            "#552F#6PTch... Exactly how I was afraid this'd\x01",
            "go down.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #42
        0x101,
        (
            "#1007F#6PAgate, you back off, too.\x01",
            "Let me handle this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Sleep(1000)
    OP_94(0x1, 0x101, 0x0, 0x15E, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #43
        0x101,
        (
            "#1002F#6POkay, Felicity, listen.\x02\x03",

            "We ARE here to take you into protective\x01",
            "custody, yes.\x02\x03",

            "#1003FAnd, look, I can totally sympathize with\x01",
            "you hating this marriage thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xC,
        (
            "#4POh, certainly, that's unforgivable\x01",
            "in and of itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        "#4PThe real problem, though, is Reina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1002F#6PWait, I'm sorry.\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        "#4PShe...betrayed me utterly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xC,
        (
            "#4PWe were SUPPOSED to be making a little\x01",
            "tourist trip out to Bose. See the market,\x01",
            "say hello to Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        (
            "#4PI've stopped by Bose briefly before,\x01",
            "but never had a chance to really see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xC,
        (
            "#4PSo you can imagine how excited I was\x01",
            "to make the trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "#4PAnd then, as soon as we arrive, what\x01",
            "do I find but an arranged marriage waiting\x01",
            "for me like a snake pit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "#4PReina had been deceiving me from the\x01",
            "very start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015F#6PNow I see... It sounds like you guys have\x01",
            "had problems for a while.\x02\x03",

            "#1002FBut, look, doesn't that make it even more\x01",
            "important to go back?\x02\x03",

            "You should meet Reina and tell her how\x01",
            "you really feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xC,
        "#4PN-No, that's...that's impossible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xC,
        "#4PI never, ever want to see Reina again.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        "#1019F#6P(Not making much progress here.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #57
        0x106,
        (
            "#552F#4P(Hey, c'mon.)\x02\x03",

            "(How long are we gonna play around?\x01",
            "She ain't gonna come willingly. We're\x01",
            "gonna have to be bastards about this.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1016F#3P(I, uh, really would rather it not come\x01",
            "to that!)\x02\x03",

            "(Gimme just a bit longer, here.\x01",
            "I'm gonna try the hard sell...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    TurnDirection(0x106, 0xC, 400)

    ChrTalk(    #59
        0x101,
        (
            "#1002F#6POkay, Felicity?\x02\x03",

            "You reeeeeally won't go back to\x01",
            "town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        "#6PAbsolutely not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        (
            "#6PAs long as Reina and that arranged marriage are\x01",
            "waiting for me, I never intend to set foot in\x01",
            "Bose again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F#6PI see...\x02\x03",

            "Well, all I have to say then is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "You really are stubborn, Felicity.\x01",      # 0
            "You really are a coward, Felicity.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBF")

    ChrTalk(    #63
        0x101,
        "#1007F#6PYou really are stubborn, Felicity.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #64
        0xC,
        "#4PI'd say it's you who's being stubborn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xC,
        (
            "#4PEven a bracer can't challenge a person's\x01",
            "life choices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xC,
        (
            "#4POr do you intend to force what you want\x01",
            "on me no matter what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1013F#6PNo, I don't want to--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xC,
        "#4PThen leave me alone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xC,
        (
            "#4PIf you keep persisting,\x01",
            "I WILL call for someone!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #70
        0x101,
        "#1008F#6PAww, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x106,
        (
            "#053F#6PSo much for persuasion.\x02\x03",

            "#057FTime for us to be sons of bitches, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x144C4, 0x0, 0xCB48, 0x7D0, 0x0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #72
        0xC,
        "#4PAieee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xC,
        "#4PWh-What are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x106,
        (
            "#057F#6PBy the powers invested in us by the International\x01",
            "Bracers' Code, Article 2, Special Provision,\x01",
            "I'm placing you under protective custody.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F#6PWait, Article 2... The Protective Duty clause,\x01",
            "right?\x02\x03",

            "But which 'special provision' do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        (
            "#053F#6PThe 'protective measures in emergencies'\x01",
            "clause.\x02\x03",

            "Remember? The regs say we can take\x01",
            "people into protective custody if they're\x01",
            "placing themselves in immediate danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1004F#6POh, yeah, I remember that clause now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        "#4PTh-That's ridiculous!\x02",
    )

    CloseMessageWindow()

    def lambda_190E():
        OP_8E(0xC, 0x144C4, 0x0, 0xC544, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_190E)
    Sleep(200)
    OP_8E(0x106, 0x144C4, 0x0, 0xC79C, 0xBB8, 0x0)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xC, 0x32, 0x0, 0x1F4, 0x7D0)

    ChrTalk(    #79
        0xC,
        (
            "#2P#3SWhat are you doing?!\x01",
            "LET ME GO!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#053F#5PYou're placing yourself in constant danger by\x01",
            "being out here unarmed, alone, and with no\x01",
            "way to contact anyone, miss.\x02\x03",

            "We're in our legal rights to take you into\x01",
            "custody. Now please, come with us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A75():

        label("loc_1A75")

        TurnDirection(0x101, 0x106, 400)
        OP_48()
        Jump("loc_1A75")

    QueueWorkItem2(0x101, 1, lambda_1A75)

    def lambda_1A86():

        label("loc_1A86")

        TurnDirection(0xF8, 0x106, 400)
        OP_48()
        Jump("loc_1A86")

    QueueWorkItem2(0xF8, 1, lambda_1A86)

    def lambda_1A97():

        label("loc_1A97")

        TurnDirection(0xF9, 0x106, 400)
        OP_48()
        Jump("loc_1A97")

    QueueWorkItem2(0xF9, 1, lambda_1A97)
    OP_43(0x106, 0x0, 0x1, 0x4)
    OP_43(0xC, 0x0, 0x1, 0x5)
    OP_43(0x101, 0x0, 0x1, 0x1)
    OP_43(0xF9, 0x2, 0x1, 0x3)

    ChrTalk(    #81 op#A op#5
        0xC,
        "#10AS-Someoooooone!\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82 op#A op#5
        0xC,
        (
            "#10AHelp, help!\x01",
            "I'm being kidnapped!\x05\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83 op#A op#5
        0x106,
        "#054F#10AStop that! Please just be quiet and walk!\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0xC, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(80870, 0, 54440, 2500)

    ChrTalk(    #84
        0x101,
        (
            "#1016FUhhh. Looks like we're taking the side\x01",
            "roads back with that, then.\x02\x03",

            "#1007F*siiigh*\x01",
            "This is so, so NOT how I wanted to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        (
            "#2PAiiiiiieeeee!\x01",
            "LET ME GO!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x97, 0x0, 0x64)

    ChrTalk(    #86
        0x106,
        "#2PC-C'mon! Quit struggling!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #87
        0xC,
        "Soldier's Voice",
        "#2PWhat's going on here?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0xC,
        "Soldier's Voice",
        "#2PThat man! Is he kidnapping her?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDC")

    ChrTalk(    #89
        0x108,
        "#070FHaha! I think we may be in trouble.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D17")

    ChrTalk(    #90
        0x103,
        "#021FI guess we're in the fryer now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1D17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8F")

    ChrTalk(    #91
        0x105,
        (
            "#045FThat, um, is Felicity, all right...\x02\x03",

            "I doubt she'll come 'quietly' for\x01",
            "the entire trip back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E09")

    label("loc_1D8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #92
        0x104,
        (
            "#031FHa-ha-ha! No less than I would expect\x01",
            "of a lady of Erebonia!\x02\x03",

            "Forceful and unyielding to the end!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E09")


    ChrTalk(    #93
        0x101,
        (
            "#1019F...C'mon, let's go help Agate.\x02\x03",

            "The last thing we need is to be SHOT AT\x01",
            "by the army on top of already feeling like\x01",
            "the worst people ever.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EA4():
        OP_6D(80870, 10000, 54440, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1EA4)
    OP_28(0x7A, 0x1, 0x20)
    Jump("loc_2DFF")

    label("loc_1EBF")


    ChrTalk(    #94
        0x101,
        "#1007F#6PYou really are a coward, Felicity.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #95
        0xC,
        "#4PI'm a WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        "#4PDid you just call me 'coward'?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1015F#6PYeah, I did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        "#4PAnd how am I a coward?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xC,
        "#4PExplain yourself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1002F#6PWell, you've been listing off a whole bunch\x01",
            "of reasons for a while now...\x02\x03",

            "But the real reason you don't want to go\x01",
            "back is because you're scared of the\x01",
            "marriage meeting, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0xC,
        "#4PI... I am not SCARED!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1002F#6PThen why not just go back to Bose and\x01",
            "confront it?\x02\x03",

            "You seem dead set on making the wedding\x01",
            "meeting out to be purely Reina's fault...\x02\x03",

            "But looking at the facts, there's no way\x01",
            "she did all this because she wanted to.\x02\x03",

            "Think about her position.\x01",
            "This can't possibly be just her fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "#4PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1010F#6PAnd yet, you're latching onto her as an excuse\x01",
            "to keep running away.\x02\x03",

            "We all run into stuff we hate in life.\x01",
            "You don't want to risk being forced into marriage;\x01",
            "I don't want to drag you back to Bose for it.\x02\x03",

            "#1002FBut if we all just try to run away from\x01",
            "it, sooner or later it catches up to us.\x02\x03",

            "I think Reina knew you'd try to run from this.\x01",
            "That's why she felt she had to lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        "#4PThat... yes, I know that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xC,
        "#4P#3SOkay, yes! You're entirely right!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        "#4P#3SThat's WHY I'm so angry at Reina!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1020F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "#4PReina always spends so much time being\x01",
            "nice to me, flattering me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "#4P#3SBut when it comes down to it, she\x01",
            "couldn't be honest to me about THIS,\x01",
            "of all things!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_24C8():

        label("loc_24C8")

        TurnDirection(0x106, 0xC, 400)
        OP_48()
        Jump("loc_24C8")

    QueueWorkItem2(0x106, 1, lambda_24C8)

    def lambda_24D9():
        OP_92(0xC, 0x101, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_24D9)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #111
        0xC,
        (
            "#4PAren't real friends supposed to trust\x01",
            "one another?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)

    def lambda_2533():
        OP_92(0xC, 0x101, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2533)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #112
        0xC,
        (
            "#4PWell, Estelle? Isn't that what friends are\x01",
            "supposed to do?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_25A7():
        OP_92(0xC, 0x101, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25A7)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x3E8, 0x0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #113
        0xC,
        "#4P#3SAnswer me! Is what I'm saying wrong?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_264A")

    ChrTalk(    #114
        0x105,
        "#043F#6PFelicity...\x02",
    )

    CloseMessageWindow()

    label("loc_264A")


    ChrTalk(    #115
        0x101,
        (
            "#1008F#6PWhoa, Felicity, wait a second...\x02\x03",

            "I'd like a second to, you know,\x01",
            "actually answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        "#4P*pant* *pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x106,
        (
            "#053F#6PYeah, now I get it.\x02\x03",

            "You've got a lot more than just an objection\x01",
            "to an arranged marriage in this.\x02\x03",

            "#050FAren't you taking it out on the wrong\x01",
            "person, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        "#4P*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        "You're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        "#4PEstelle isn't the one who needs my venom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        "#4PI need to save this anger for Reina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1011F#6PWait, so...you'll go back with us?\x02\x03",

            "You're sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xC,
        "#4PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "#4PI do feel a little more clearheaded now\x01",
            "that I've managed to spit all that out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        "#4PFor now...let's go back to Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "#4PI need to let Reina know how much she\x01",
            "hurt me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295F")

    ChrTalk(    #127
        0x105,
        (
            "#542F#6PPhew! Thank goodness.\x02\x03",

            "I'm glad this ended somewhat\x01",
            "well, at any rate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C9")

    ChrTalk(    #128
        0x103,
        (
            "#020FWe don't have to leave right this second\x01",
            "if you still need a moment, Felicity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEC")

    label("loc_29C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A6F")

    ChrTalk(    #129
        0x108,
        (
            "#070FHaha, we're no longer screaming at each\x01",
            "other, at least!\x02\x03",

            "You are sure you're ready, however?\x01",
            "We could wait here a little longer,\x01",
            "perhaps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEC")

    label("loc_2A6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEC")

    ChrTalk(    #130
        0x104,
        (
            "#030FI do not think the need so pressing that\x01",
            "we could not take a moment longer to rest,\x01",
            "should you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEC")


    ChrTalk(    #131
        0xC,
        "#4PNo, I'm all right. And Estelle has a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xC,
        (
            "#4PI can't just run from this.\x01",
            "I need to confront what's being forced on\x01",
            "me and let everyone know what I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1001F#6PHeehee! That's the spirit. ♪\x02\x03",

            "#1017FSorry. I know I was kinda playing\x01",
            "hard-ball there for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        (
            "#4PNo, I should be the one to apologize...\x01",
            "I know that you know the answer to that\x01",
            "question already, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "#4PLet us be off, then, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        (
            "#4PAfter all, I will need your escort...\x01",
            "on the way home.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D0B")

    ChrTalk(    #137
        0x108,
        "#070FLeave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DAD")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D50")

    ChrTalk(    #138
        0x104,
        (
            "#031FBut of course!\x01",
            "You are safe in our hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DAD")

    label("loc_2D50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D86")

    ChrTalk(    #139
        0x103,
        "#525FOf course, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DAD")

    label("loc_2D86")


    ChrTalk(    #140
        0x101,
        "#1006F#6PYeah, leave it to us! ♪\x02",
    )

    CloseMessageWindow()

    label("loc_2DAD")


    ChrTalk(    #141
        0x106,
        "#051F#6PLet's get this show on the road, then.\x02",
    )

    CloseMessageWindow()

    def lambda_2DE7():
        OP_6D(82800, 10000, 53860, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2DE7)
    OP_28(0x7A, 0x1, 0x10)

    label("loc_2DFF")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1131   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_2E1E(): pass

    label("Function_1_2E1E")

    Sleep(200)
    OP_8F(0x101, 0x144D8, 0x0, 0xD2BE, 0x7D0, 0x0)
    Return()

    # Function_1_2E1E end

    def Function_2_2E38(): pass

    label("Function_2_2E38")

    Sleep(400)
    OP_8F(0xF8, 0x13470, 0x0, 0xD5D4, 0x7D0, 0x0)
    Return()

    # Function_2_2E38 end

    def Function_3_2E52(): pass

    label("Function_3_2E52")

    Sleep(1000)
    OP_6D(78140, 0, 53020, 3000)
    Return()

    # Function_3_2E52 end

    def Function_4_2E69(): pass

    label("Function_4_2E69")

    OP_8E(0x106, 0x144C4, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_8E(0x106, 0x1426C, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_A6(0x6)
    OP_8E(0x106, 0x124F8, 0x0, 0xCE2C, 0x7D0, 0x0)

    def lambda_2EAE():
        OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2EAE)
    OP_8E(0x106, 0x11FE4, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_8E(0x106, 0x11BFC, 0x0, 0xCE2C, 0x7D0, 0x0)
    Return()

    # Function_4_2E69 end

    def Function_5_2EE3(): pass

    label("Function_5_2EE3")

    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xC, 0x40)
    OP_8F(0xC, 0x144C4, 0x0, 0xCB48, 0x7D0, 0x0)
    OP_8F(0xC, 0x144C4, 0x0, 0xCF08, 0x7D0, 0x0)
    OP_A2(0x6)
    OP_8C(0xC, 90, 0)
    OP_8F(0xC, 0x124F8, 0x0, 0xCE2C, 0x7D0, 0x0)

    def lambda_2F46():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2F46)
    OP_8F(0xC, 0x11FE4, 0x0, 0xCE2C, 0x7D0, 0x0)
    Return()

    # Function_5_2EE3 end

    SaveToFile()

Try(main)
