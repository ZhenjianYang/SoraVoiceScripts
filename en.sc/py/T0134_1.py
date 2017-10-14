from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0134_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0134_1 ._SN',
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
        "Function_1_8FC",          # 01, 1
        "Function_2_A99",          # 02, 2
        "Function_3_1C13",         # 03, 3
        "Function_4_21F7",         # 04, 4
        "Function_5_22EF",         # 05, 5
        "Function_6_23BB",         # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_17F")

    ChrTalk(    #0
        0xD,
        (
            "#6PI can hardly see the stars with all\x01",
            "this fog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xD,
        (
            "#6PAnd yet I care not for the glittering\x01",
            "sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xD,
        (
            "#6PFor you, my love, are only star\x01",
            "I need to guide me through the\x01",
            "darkest nights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F")


    ChrTalk(    #3
        0x101,
        (
            "#1007F#3PAhem!\x02\x03",

            "Ummm, may I have a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #4
        0xD,
        "#6PHmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_1DC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1DC)
    Sleep(250)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #5
        0xE,
        "#2POh? Who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1000F#3PI'm with the Bracer Guild.\x02\x03",

            "You're Armand, right? I saw your\x01",
            "request on the bulletin board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        "Ah, you really came!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        "Thank you! I've been waiting so long!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #9
        0xE,
        (
            "#2PThis is wonderful, Armand!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #10
        0xD,
        "#6PAhh, Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        "#6PWhy is your heart so beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "#6PEven though I am the cause of\x01",
            "your suffering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xE,
        "#2PDon't say that, Armand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "#2PI know best just how hard this\x01",
            "is on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        (
            "#2PWe promised on that night, didn't we?\x01",
            "That you and I, no matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xD,
        (
            "#6PWe would hold hands and live out\x01",
            "our days together, good and bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        "#6POh, I love you, Ellie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        "#2PAnd I you, Armand!\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50E")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_54C")

    label("loc_50E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_535")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_54C")

    label("loc_535")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_54C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5B1")

    label("loc_573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5B1")

    label("loc_59A")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_5B1")

    Sleep(1000)

    ChrTalk(    #19
        0x101,
        (
            "#1016F#3PUmmmm...\x02\x03",

            "Didn't you have some kind of request?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #20
        0xD,
        "#6PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xE,
        "#2PThat's right, the request!\x02",
    )

    CloseMessageWindow()

    def lambda_643():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_643)
    Sleep(150)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #22
        0xD,
        (
            "W-Well, to make it short, this request\x01",
            "is so important that it directly affects\x01",
            "our future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "In fact, I'd like you to start investigating\x01",
            "immediately if you can. Can you?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    Call(1, 2)
    Jump("loc_8E3")

    label("loc_75C")


    ChrTalk(    #24
        0x101,
        (
            "#1015F#3PAh, er, sorry.\x02\x03",

            "I'm afraid we can't start right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        "N-Nooo... Don't abandon us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        "#2PPlease... This is very important!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#020FIt's okay. We'll be back soon,\x01",
            "so please relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1000F#3PYeah, we'll be back the second\x01",
            "we have time to hear what you\x01",
            "have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        "R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        "A-All right... I believe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        (
            "#2PCome back soon, please.\x01",
            "For our love!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x8000)

    label("loc_8E3")

    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_8FC(): pass

    label("Function_1_8FC")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_8C(0xD, 270, 0)
    OP_8C(0xE, 270, 0)
    OP_0D()

    ChrTalk(    #32
        0xD,
        "Oh, hello again, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xD,
        (
            "Are you ready to hear our\x01",
            "request?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AE")
    Call(1, 2)
    Jump("loc_A80")

    label("loc_9AE")


    ChrTalk(    #34
        0x101,
        "#1007FTo be honest, we're still a bit busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        "N-Nooooooooooo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1016FSorry, sorry! I know it's important.\x01",
            "We'll be back to hear you out soon,\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "Come back soon, please.\x01",
            "For our love!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A80")

    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_1_8FC end

    def Function_2_A99(): pass

    label("Function_2_A99")


    ChrTalk(    #38
        0x101,
        "#1006FYep! We're all squared away.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA0")

    ChrTalk(    #39
        0xD,
        "R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#020FWe're in a hurry, though,\x01",
            "so make it quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        "Of course, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "Bless you, bracers! Bless your\x01",
            "loving hearts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "You have NO idea how much\x01",
            "I appreciate you doing this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE3")

    label("loc_BA0")


    ChrTalk(    #44
        0xD,
        "R-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "Bless you, bracers! Bless your\x01",
            "loving hearts!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE3")

    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #46
        0xE,
        (
            "#2PHow wonderful, Armand!\x01",
            "I'm so happy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #47
        0xD,
        "#6PAhh, Ellie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        "#6PWhy is your heart so beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        "#2POooh, Armand...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #50
        0x101,
        (
            "#1019F#4SSo...#2S\x02\x03",

            "...about that request.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CAE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CAE)
    Sleep(150)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #51
        0xD,
        "...Pardon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "Ahem! Yes. Let me explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020FYes, please do.\x01",
            "As simply and swiftly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "What I'd like to ask of you all\x01",
            "is nothing less than finding our\x01",
            "engagement ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "I scraped and saved up all the\x01",
            "mira I could to get a really nice\x01",
            "ring, but then...then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "Th-That cursed crow snatched\x01",
            "it from me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x101,
        "#1004F#3PC-Crow?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(    #58
        0x107,
        "#064FCrow? Like a bird?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_E77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB1")

    ChrTalk(    #59
        0x105,
        "#044FYou mean like the bird, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_EB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE2")

    ChrTalk(    #60
        0x104,
        "#033FCrow? As in the bird?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_EE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F19")

    ChrTalk(    #61
        0x106,
        "#052FYou mean like the bird, right?\x02",
    )

    CloseMessageWindow()

    label("loc_F19")


    ChrTalk(    #62
        0xD,
        (
            "Yes! The ones that go, 'caw!'\x01",
            "and bring suffering to those\x01",
            "in love!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "One of those dastardly things\x01",
            "flew off with our ring in his mouth!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_140D")

    ChrTalk(    #64
        0x103,
        (
            "#026FHa. Well, crows are known to\x01",
            "have an eye for anything shiny.\x02\x03",

            "#027FStill... A ring and a crow... Hmm...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #65
        0x101,
        (
            "#7P#1011FHmm?\x02\x03",

            "Schera, are you thinking what\x01",
            "I'm thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#020FI believe I am. We should have\x01",
            "them take a look just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        "Did you think of something?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1002FArmand, would you take\x01",
            "a look at this ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70 op#A
        0xD,
        (
            "#22ASure, I don't mi...\x01",
            "WHOA! THIS IS IT!\x02",
        )
    )
    Sleep(2300)

    Call(1, 5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        "#1004FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BA")

    ChrTalk(    #72
        0x107,
        "#064FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_11BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #73
        0x105,
        "#044FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_11E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_120E")

    ChrTalk(    #74
        0x104,
        "#033FAre you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_120E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1233")

    ChrTalk(    #75
        0x106,
        "#055FYou sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_1233")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1255")

    ChrTalk(    #76
        0x108,
        "#073FYou sure?\x02",
    )

    CloseMessageWindow()

    label("loc_1255")


    ChrTalk(    #77
        0xD,
        "Yes, I'm ABSOLUTELY sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        "This is our ring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "#2PI cannot thank you enough for\x01",
            "your kindness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#021FLooks like my hunch was right\x01",
            "on the mira.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1330")

    ChrTalk(    #81
        0x108,
        "#073FTalk about a crazy coincidence.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_1330")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136B")

    ChrTalk(    #82
        0x106,
        "#052FTalk about a crazy coincidence.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_136B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A5")

    ChrTalk(    #83
        0x104,
        "#031FHahaha. My, how serendipitous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_13A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DA")

    ChrTalk(    #84
        0x105,
        "#044FWhat an amazing coincidence!\x02",
    )

    CloseMessageWindow()

    label("loc_13DA")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x8)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_63(0xF)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Jump("loc_1C12")

    label("loc_140D")


    ChrTalk(    #85
        0x103,
        (
            "#027FHa. Well, crows are known to\x01",
            "have an eye for anything shiny.\x02\x03",

            "A sparkling ring sounds just like\x01",
            "their idea of a new toy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1015F#3PThat ring's probably in some\x01",
            "bird's nest by now, huh?\x02\x03",

            "#1002FAnd you want us to find it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xD,
        "Please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xD,
        (
            "I'm well aware of how much of \x01",
            "a challenge this is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xD,
        (
            "Even so, I dearly hope you'll find it.\x01",
            "Somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1007F#3PI mean, I want to find it, too, but...\x02\x03",

            "We don't have a whole lot of info\x01",
            "to work with here. Just knowing a\x01",
            "crow took it isn't all that much.\x02\x03",

            "#1002FDo you have any more clues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xD,
        (
            "Well, I have some idea of where\x01",
            "its nest is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        "I'm pretty sure it's north of Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        (
            "The crow flew off towards the\x01",
            "Malga Trail after it was done\x01",
            "plundering our hopes and dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "I would have given chase, but with\x01",
            "the fog and all...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1885")

    ChrTalk(    #95
        0x101,
        (
            "#1015F#3PHa, no worries. I understand.\x02\x03",

            "So the nest's probably to the north...\x02\x03",

            "...Wait? To the north?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #96
        0x101,
        (
            "#1019F#3P(N-No way!)\x02\x03",

            "(What if it's that ring we found\x01",
            "at the top of the tower?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        "Mm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1016F#3PN-No, it's nothing.\x01",
            "(Eh, I'm sure it's just a coincidence.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C2")

    label("loc_1885")


    ChrTalk(    #99
        0x101,
        (
            "#1015F#3PI see.\x02\x03",

            "So the nest's probably to the north...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C2")


    ChrTalk(    #100
        0x103,
        "#026FWe'll take that under advisement.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195B")

    ChrTalk(    #101
        0x108,
        (
            "#075FYeah, no other leads, really.\x02\x03",

            "This request is going to be\x01",
            "a real pain, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_195B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B8")

    ChrTalk(    #102
        0x106,
        (
            "#551FYeah, got no other choice.\x02\x03",

            "This is gonna be a pain in the\x01",
            "ass...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_19B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4C")

    ChrTalk(    #103
        0x104,
        (
            "#034FNot much else we can do, really.\x02\x03",

            "*sigh* This looks like a job that's\x01",
            "going to require a lot of finesse...\x01",
            "and patience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8C")

    ChrTalk(    #104
        0x105,
        (
            "#047FAfraid there isn't much else we\x01",
            "CAN do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8C")


    ChrTalk(    #105
        0xD,
        (
            "We have no choice but to rely\x01",
            "on the guild at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        (
            "Please, PLEASE do everything\x01",
            "you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "#2PYou bracers are our only hope.\x01",
            "Please, you must find it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1006F#3PWe'll do whatever we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        (
            "#020FWe'll come back and report\x01",
            "once we know more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xD,
        (
            "We'll be right here! Our hope\x01",
            "--and our future--rests with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        "#2PGood luck!\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x4, 0x4)
    OP_28(0x72, 0x4, 0x8)
    OP_28(0x72, 0x1, 0x1)
    OP_28(0x72, 0x1, 0x2)
    OP_A2(0x7)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)

    label("loc_1C12")

    Return()

    # Function_2_A99 end

    def Function_3_1C13(): pass

    label("Function_3_1C13")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1CDF")

    ChrTalk(    #112
        0xD,
        (
            "I can hardly see the stars with all\x01",
            "this fog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        (
            "And yet I care not for the glittering\x01",
            "sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "For you, my love, are only star\x01",
            "I need to guide me through the\x01",
            "darkest nights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDF")


    ChrTalk(    #115
        0x101,
        "#1007F(They're still at it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    def lambda_1D16():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1D16)
    Sleep(250)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #117
        0xE,
        "#2PYou're back!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)

    ChrTalk(    #118
        0xD,
        "D-Did you find our ring?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#020FWe've found a ring that matches\x01",
            "your description, at least.\x02\x03",

            "We'll need to have you identify it\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1000FYep. We just need you to confirm\x01",
            "if it's yours or not.\x02\x03",

            "Armand, could you take a look at\x01",
            "this ring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121 op#A
        0xD,
        "#22ASure, I don't mi...\x02",
    )
    Sleep(2000)

    Call(1, 5)

    ChrTalk(    #122
        0x101,
        "#1004FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB6")

    ChrTalk(    #123
        0x107,
        "#064FSeriously?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE1")

    ChrTalk(    #124
        0x105,
        "#044FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0C")

    ChrTalk(    #125
        0x104,
        "#033FA-Are you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F35")

    ChrTalk(    #126
        0x106,
        "#055FAre you sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F57")

    label("loc_1F35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F57")

    ChrTalk(    #127
        0x108,
        "#073FYou sure?\x02",
    )

    CloseMessageWindow()

    label("loc_1F57")


    ChrTalk(    #128
        0xD,
        "You sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        "Yes, I'm ABSOLUTELY sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "#2PI cannot thank you enough for\x01",
            "your kindness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        (
            "#021FGood to hear! Makes this all\x01",
            "worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_204E")

    ChrTalk(    #132
        0x108,
        (
            "#070FMission complete!\x02\x03",

            "Didn't expect we'd find it in\x01",
            "such a bizarre spot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_204E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CC")

    ChrTalk(    #133
        0x105,
        (
            "#040FGood... That settles things, then.\x02\x03",

            "I never dreamed we would find it\x01",
            "in a place like that, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_20CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(    #134
        0x106,
        (
            "#051FGood to hear. Nice to finally\x01",
            "wrap this thing up.\x02\x03",

            "Never thought we'd find it in\x01",
            "such a weird spot, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_2153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CC")

    ChrTalk(    #135
        0x104,
        (
            "#030FA job well done!\x02\x03",

            "I certainly never dreamed the\x01",
            "request would take us where\x01",
            "we ended up, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CC")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_63(0xF)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_3_1C13 end

    def Function_4_21F7(): pass

    label("Function_4_21F7")

    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    SetChrPos(0x101, 62800, 0, 47270, 90)
    SetChrPos(0x103, 61790, 0, 46800, 90)
    SetChrPos(0xF8, 61270, 0, 47980, 90)
    SetChrPos(0xF9, 60320, 0, 47290, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2272")
    SetChrPos(0xF9, 61270, 0, 47980, 90)
    SetChrPos(0xF8, 60320, 0, 47290, 90)

    label("loc_2272")

    OP_6D(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_21F7 end

    def Function_5_22EF(): pass

    label("Function_5_22EF")

    OP_94(0x1, 0xD, 0x0, 0xC8, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_2323():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2323)
    Sleep(900)
    OP_63(0xD)
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #136
        0xD,
        "#3SAaaaaaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "Th-Th-That's the ring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xD,
        "#3SThat's it! That's our engagement ring!!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_5_22EF end

    def Function_6_23BB(): pass

    label("Function_6_23BB")


    ChrTalk(    #139
        0x101,
        (
            "#1015FPhew! Man...\x02\x03",

            "Yeah, never thought we'd find\x01",
            "your ring on the roof of the tower.\x02\x03",

            "#1000FHere, let me give it back to you\x01",
            "before it ends up lost again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #140
        "\x07\x00Handed over #564i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x234, 1)
    OP_94(0x1, 0xD, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #141
        0xD,
        "Th-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xD,
        (
            "I... I don't even know how to express\x01",
            "how I feel right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        (
            "#2PTeehee! We never lost our faith\x01",
            "in you. Thank you so, so much. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#1017FNot at all. I'm glad we could help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x103,
        (
            "#020FYour wedding isn't too far off\x01",
            "from now, is it?\x02\x03",

            "#525FBest wishes! ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #146
        0xE,
        "#2PTh-Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        (
            "#2PGoodness, it's a little embarrassing\x01",
            "to hear it said out loud...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #148
        0xD,
        "#6PDon't be embarrassed, my love.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "#6PFor no other love has received a\x01",
            "stronger blessing. We still have\x01",
            "a lifetime of well wishes ahead of us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #150
        0xE,
        "#2PArmand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        "#6PEllie...\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1800, 0xA, 0xB, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2787")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_27C5")

    label("loc_2787")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27AE")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_27C5")

    label("loc_27AE")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_27C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27EC")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_282A")

    label("loc_27EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2813")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_282A")

    label("loc_2813")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_282A")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287B")

    ChrTalk(    #152
        0x107,
        (
            "#067F(Awww...\x01",
            "They're off in their own little world.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2947")

    label("loc_287B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C0")

    ChrTalk(    #153
        0x105,
        "#540F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2947")

    label("loc_28C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2905")

    ChrTalk(    #154
        0x104,
        "#030F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2947")

    label("loc_2905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2947")

    ChrTalk(    #155
        0x108,
        "#070F(Off in their own little world, I see...)\x02",
    )

    CloseMessageWindow()

    label("loc_2947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2986")

    ChrTalk(    #156
        0x106,
        "#552F(Watching this makes my head hurt.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_2986")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B9")

    ChrTalk(    #157
        0x108,
        "#071F(Truly, love is blind.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_29B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FD")

    ChrTalk(    #158
        0x104,
        "#031F(You know what they say: Love is blind.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_29FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A31")

    ChrTalk(    #159
        0x105,
        "#048F(Haha, I think it's sweet.)\x02",
    )

    CloseMessageWindow()

    label("loc_2A31")


    ChrTalk(    #160
        0x103,
        (
            "#020F(Anyway, it'd be rude to interrupt them,\x01",
            "so...let's excuse ourselves.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1013F(Yes! Good idea! Let's go, go, go!)\x02\x03",

            "#1016FWell, pardon us, lovebirds.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #162
        "Quest #2C[The Ring That Flew Away] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    OP_A2(0x6)
    Return()

    # Function_6_23BB end

    SaveToFile()

Try(main)
